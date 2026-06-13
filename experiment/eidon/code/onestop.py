import json
import random
from dataclasses import dataclass

from eidon.build import ExperimentType, stimuli
from eidon.fonts import FONTS
from PIL import Image, ImageDraw, ImageFont


@dataclass
class OneStop(ExperimentType):
    margin: int
    font_size: int
    line_spacing: int

    def build(self, experiment_path):
        with open(experiment_path / "materials" / "onestop_qa.json", "r") as f:
            data = json.load(f)["data"][:1]  # Only use the first article

        (instructions_image,) = stimuli.generate_text_pages(
            "A paragraph will appear on screen. Read the paragraph, then press [SPACE]. Then, you will see a multiple-choice comprehension question about the paragraph. Select the correct answer by pressing [UP], [DOWN], [LEFT], or [RIGHT].\n\nThere will be six paragraphs in total.\n\nPress [SPACE] to start.",
            *self.display_size,
            self.margin,
            FONTS["default"],
            self.font_size,
            line_spacing=self.line_spacing,
            vertical_align="center",
            background_color=self.background_color,
        )
        instructions_image.save(experiment_path, "instructions")

        (end_image,) = stimuli.generate_text_pages(
            "This is the end of the experiment. Thank you for your participation!",
            *self.display_size,
            self.margin,
            FONTS["default"],
            self.font_size,
            line_spacing=self.line_spacing,
            vertical_align="center",
            background_color=self.background_color,
        )
        end_image.save(experiment_path, "end")

        trial_stages = []
        for article_id, article in enumerate(data):
            for paragraph_id, paragraph in enumerate(article["paragraphs"]):
                paragraph_name = f"paragraph{article_id}_{paragraph_id}"

                text = paragraph["Adv"]["context"]
                qa = paragraph["qas"][0]  # Only use the first question for each paragraph
                question = qa["question"]
                answers = qa["answers"]
                random.shuffle(answers)

                (text_image,) = stimuli.generate_text_pages(
                    text,
                    *self.display_size,
                    self.margin,
                    FONTS["default"],
                    self.font_size,
                    line_spacing=self.line_spacing,
                    vertical_align="center",
                    background_color=self.background_color,
                )
                text_image.save(
                    experiment_path,
                    f"{paragraph_name}.text",
                )
                text_start_location = (
                    int(text_image.areas["page"][0].left - self.font_size),
                    int(
                        text_image.areas["page"][0].top
                        + self.font_size * self.line_spacing / 2
                    ),
                )
                trial_stages.append(
                    {
                        "$name": f"{paragraph_name}.drift",
                        "$type": "DriftCorrect",
                        "location": text_start_location,
                    }
                )
                trial_stages.append(
                    {
                        "$name": f"{paragraph_name}.text",
                        "$type": "StimulusPage",
                        "imgpath": f"stimuli/{paragraph_name}.text.png",
                        "continue_key": "SPACE",
                    }
                )

                question_image = self._generate_mcq_page(question, answers)
                question_image.save(
                    experiment_path,
                    f"{paragraph_name}.question",
                )
                trial_stages.append(
                    {
                        "$name": f"{paragraph_name}.question",
                        "$type": "MultipleChoiceQuestion",
                        "imgpath": f"stimuli/{paragraph_name}.question.png",
                        "option_keys": ["UP", "LEFT", "RIGHT", "DOWN"],
                        "option_boxes": [
                            area.xywh
                            for area in question_image.areas["section"]
                            if area.content.startswith("option:")
                        ],
                        "confirm_key": "SPACE",
                    }
                )

        stages = [
            {"$name": "setup", "$type": "Setup"},
            {
                "$name": "instructions",
                "$type": "StimulusPage",
                "imgpath": "stimuli/instructions.png",
                "continue_key": "SPACE",
            },
            *trial_stages,
            {
                "$name": "end",
                "$type": "StimulusPage",
                "imgpath": "stimuli/end.png",
                "continue_key": "SPACE",
            },
        ]

        return {"P1": {"stages": stages}}

    def _generate_mcq_page(
        self,
        question: str,
        options: list[str],
        text_color: tuple[int, int, int] = (0, 0, 0),
        extend_word_areas: bool = True,
    ) -> stimuli.TextImage:
        width, height = self.display_size
        margin = self.margin
        font_path = FONTS["default"]
        font_size = self.font_size
        line_spacing = self.line_spacing
        background_color = self.background_color
        vertical_align = "center"

        text_width = width - 2 * margin
        text_height = height - 2 * margin

        image = Image.new("RGB", (width, height), tuple(background_color))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_path, font_size)

        num_question_lines = len(list(stimuli.wrap_text(question, font, text_width)))

        font_ascent, font_descent = font.getmetrics()
        line_height = (font_ascent + font_descent) * line_spacing

        option_width = text_width / 2
        option_height = line_height * 2
        option_centers = [
            (width / 2, line_height * 2),
            (margin + option_width / 2, line_height * 2 + option_height),
            (width - margin - option_width / 2, line_height * 2 + option_height),
            (width / 2, line_height * 2 + option_height * 2),
        ]

        total_height = num_question_lines * line_height + 8 * line_height

        question_left = margin
        question_top = margin
        if vertical_align == "center":
            question_top += (text_height - total_height) / 2
        elif vertical_align == "bottom":
            question_top += text_height - total_height
        question_bottom = question_top + num_question_lines * line_height
        question_width = text_width

        char_areas = []
        word_areas = []
        section_areas = []

        question_char_areas, question_word_areas, question_area = stimuli.draw_text(
            draw,
            question,
            question_left,
            question_top,
            question_width,
            font,
            line_spacing=line_spacing,
            extend_word_areas=extend_word_areas,
            max_height=text_height,
            color=text_color,
        )
        for char_area in question_char_areas:
            char_area.section = "question"
        for word_area in question_word_areas:
            word_area.section = "question"
        question_area.content = "question"
        char_areas.extend(question_char_areas)
        word_areas.extend(question_word_areas)
        section_areas.append(question_area)

        # Draw answer options
        for option_index, option in enumerate(options):
            option_left = option_centers[option_index][0] - option_width / 2
            option_top = (
                question_bottom + option_centers[option_index][1] - option_height / 2
            )
            # Draw option text
            option_char_areas, option_word_areas, option_area = stimuli.draw_text(
                draw,
                option,
                option_left,
                option_top,
                option_width,
                max_height=option_height,
                font=font,
                align="center",
                vertical_align="center",
                line_spacing=line_spacing,
                extend_word_areas=extend_word_areas,
                color=text_color,
            )
            for char_area in option_char_areas:
                char_area.section = f"option:{option_index}"
            for word_area in option_word_areas:
                word_area.section = f"option:{option_index}"
            option_area.content = f"option:{option_index}"
            char_areas.extend(option_char_areas)
            word_areas.extend(option_word_areas)
            section_areas.append(option_area)

        return stimuli.TextImage(
            image, {"char": char_areas, "word": word_areas, "section": section_areas}
        )

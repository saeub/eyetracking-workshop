## Analyzing eye-tracking data

In this exercise, you will explore a small subset of the [OneStop dataset](https://lacclab.github.io/OneStop-Eye-Movements/index.html).

### Download this repository

[Download this repository as a ZIP file](https://github.com/saeub/eyetracking-workshop/archive/refs/heads/main.zip) and extract its contents. Make sure you remember where the folder `eyetracking-workshop-main` is located on your file system.

### Data structure

`paragraph_dwell_times.csv` contains dwell times for word-level areas of interest (AOIs) on the **paragraph screen**. It is a table with the following columns:

| Column name      | Description                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| `participant_id` | The identifier of the participant                                                                |
| `paragraph_id`   | The identifier of the paragraph being read (unique within the paragraph)                         |
| `aoi_id`         | The identifier of the AOI (unique within the question)                                           |
| `aoi_text`       | The text in the AOI that is being fixated                                                        |
| `dwell_time`     | The total time spent fixating the AOI (in milliseconds)                                          |

`question_dwell_times.csv` contains dwell times for word-level areas of interest (AOIs) on the **question screen**. It is a table with the following columns:

| Column name      | Description                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| `participant_id` | The identifier of the participant                                                                |
| `paragraph_id`   | The identifier of the paragraph being read (unique within the paragraph)                         |
| `region`         | The region that is being fixated (`question`, `answer_A`, `answer_B`, `answer_C`, or `answer_D`) |
| `region_text`    | The text in the region that is being fixated (either a question or an answer option)             |
| `aoi_id`         | The identifier of the AOI (unique within the question)                                           |
| `aoi_text`       | The text in the AOI that is being fixated                                                        |
| `dwell_time`     | The total time spent fixating the AOI (in milliseconds)                                          |

The questions are structured according to the [STARC framework](https://doi.org/10.18653/v1/2020.acl-main.507), which requires the four answer options to follow a specific pattern:

- **A**: correct answer
- **B**: incorrect answer representing a plausible misunderstanding of the part containing the correct answer
- **C**: incorrect answer referring to a part of the paragraph that does not contain the correct answer
- **D**: incorrect answer that is plausible a-priori but not supported by the paragraph

The order of the answer options was randomized during the experiment.

### Tasks

You can solve these tasks with any data analysis software you are familiar with, e.g., Excel, Stata, SPSS, R, or Python. We strongly recommend working in pairs with someone who uses the same software as you, so that you can help each other.

Feel free to pick the tasks that are most interesting to you.

#### Analyzing dwell times on the paragraphs:

- Which words tend to be fixated longer?
- What effect does word frequency have on dwell times?
- Did participants who answered the question incorrectly show different reading speeds?

#### Analyzing dwell times on the comprehension questions:

- Which distractor type (B, C, or D) attract the most attention?
- Is this pattern the same for every question?
- Does the length of the answer option have an effect on the dwell time?
- Did participants who answered the question incorrectly show different attention patterns?

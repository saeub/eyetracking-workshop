# Workshop: Introduction to Eye-Tracking for Language and Education Research

Authors: Andreas Säuberli, Gabrielle Gaudeau, Hongyi Yang

This repository contains the material used during the hands-on part of the workshop.

> To follow the workshop, you will need **a laptop with your preferred software for data analysis installed** (e.g. Excel, R, Python, Stata, SPSS, or other software packages will work).

### [➡️ Data analysis tasks](dataset/README.md)

The source of the material is the [OneStop dataset](https://lacclab.github.io/OneStop-Eye-Movements/index.html) by [Berzak et al., 2025](https://doi.org/10.1038/s41597-025-06272-2). The original dataset contains eye-tracking data from 360 L1 participants reading a total of 162 English paragraphs and answering multiple-choice comprehension questions. The experiment and dataset for the workshop only include six paragraphs with one question each.

## Eye-tracking experiment

There are several open-source software toolkits for implementing and running eye-tracking experiments. This repository contains two implementations using different toolkits:

- [**PsychoPy**](https://psychopy.org/) is a popular solution across disciplines from psychophysics to linguistics, and offers a lot of flexibility for implementing all kinds of experiments, including eye tracking, but it lacks some features that are useful for reading experiments. It features a graphical user interface (GUI). For detailed customization, programming in Python is required.
- [**eidon**](https://saeub.github.io/eidon/) is a new toolkit that is optimized for text-based eye-tracking experiments. It provides configurable implementations for common experimental paradigms in psycholinguistics and NLP. It does not have a GUI and uses a command-line interface. For detailed customization, programming in Python is required.

If you do not know how to use a terminal / command-line interface, we recommend starting with **PsychoPy**.

### [➡️ Instructions for running the PsychoPy experiment](experiment/psychopy/README.md)

### [➡️ Instructions for running the eidon experiment](experiment/eidon/README.md)

## Eye-tracking dataset

The dataset is a subset of OneStop that includes word-level dwell time as an eye-tracking measure. See the instructions for more details and exercise tasks.

### [➡️ Instructions for analyzing the dataset](dataset/README.md)

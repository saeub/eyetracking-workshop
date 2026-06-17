## Running the eidon experiment

### 1. Download this repository

[Download this repository as a ZIP file](https://github.com/saeub/eyetracking-workshop/archive/refs/heads/main.zip) and extract its contents. Make sure you remember where the folder `eyetracking-workshop-main` is located on your file system.

### 2. Install _eidon_

You need Python 3.10 or newer to run the experiment.

The easiest way to install _eidon_ is using `pip` via the terminal. Creating a virtual environment is recommended.

```bash
pip install eidon
```

> Optional: To run the experiment with an EyeLink eye tracker, you also need to run `pip install sr-research-pylink`. Note that Python versions newer than 3.12 are currently not supported by EyeLink.

### 3. Run the experiment

In the terminal, navigate to the experiment folder (`eyetracking-workshop-main/experiment/eidon). Then run this command:

```bash
eidon run . P1 --dummy
```

`.` represents the current directory (i.e. the experiment folder). `P1` is the participant ID (for the sake of demonstration, there is only one participant ID in this experiment). `--dummy` means you are testing the experiment without an eye tracker.

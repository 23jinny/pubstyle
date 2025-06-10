# Contributing to pubstyle

First off, thank you for considering contributing to `pubstyle`! Your help is appreciated. This guide will provide you with all the information you need to contribute to the project.

## Table of Contents

- [Contributing to pubstyle](#contributing-to-pubstyle)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [Setting Up Your Development Environment](#setting-up-your-development-environment)
  - [Project Structure](#project-structure)
  - [How to Add a New Style](#how-to-add-a-new-style)
  - [Submitting Your Contribution](#submitting-your-contribution)

## Code of Conduct

This project and everyone participating in it is governed by a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Setting Up Your Development Environment

To get started, you'll need to have Python 3.7+ and `git` installed. Then, follow these steps:

1. **Fork the repository** on GitHub.

2. **Clone your fork** locally:

    ```bash
    git clone https://github.com/YOUR_USERNAME/pubstyle.git
    cd pubstyle
    ```

3. **Install the package in editable mode**:
    This is the recommended way to install for development. It will install the package, but any changes you make to the source code will be immediately reflected without needing to reinstall.

    ```bash
    python -m pip install -e .
    ```

    This command also installs all the necessary dependencies, like `matplotlib`.

4. **Verify the installation** by running the CLI tool:

    ```bash
    pubstyle-cli
    ```

    This should print the current style configuration.

## Project Structure

The project is organized as follows:

```text
pubstyle/
├── assets/                 # Contains images for the README.
├── docs/                   # Contains other documentation (e.g., packaging_guide.md).
├── pubstyle/               # The main source code for the package.
│   ├── __init__.py         # Makes the directory a package and exposes the public API.
│   ├── _styles_config.py   # Defines the dictionaries of style parameters.
│   ├── styles.py           # Contains the core functions that apply the styles.
│   └── cli.py              # The command-line interface logic.
├── .gitignore              # Specifies files for Git to ignore.
├── CODE_OF_CONDUCT.md      # Code of Conduct for contributors.
├── CONTRIBUTING.md         # This contribution guide.
├── LICENSE                 # The project's license.
├── pyproject.toml          # The main configuration file for packaging and dependencies.
└── README.md               # The main project README.
```

- **`pubstyle/styles.py`**: This is where the main logic lives. Functions like `apply_paper_style` take style parameters and apply them to `matplotlib.rcParams`.
- **`pubstyle/_styles_config.py`**: This file contains the style dictionaries (e.g., `PAPER_STYLE_PARAMS`). The leading underscore suggests it's for internal use within the package.
- **`pubstyle/cli.py`**: This file contains the logic for the `pubstyle-cli` command, which allows users to inspect styles and generate sample plots.

## How to Add a New Style

Adding a new style (e.g., for a specific journal or a different aesthetic) is the most common way to contribute. Here’s a step-by-step guide:

1. **Define the Style Parameters in `_styles_config.py`**:
    - Open `pubstyle/_styles_config.py`.
    - Create a new dictionary for your style. Use a descriptive name in all caps, like `JOURNAL_STYLE_PARAMS`.
    - Populate this dictionary with the `matplotlib` rcParams you want to set. You can use `PAPER_STYLE_PARAMS` as a template.

2. **Create the Style Application Function in `styles.py`**:
    - Open `pubstyle/styles.py`.
    - Create a new function, e.g., `apply_journal_style()`.
    - This function should accept `use_latex=False` and `custom_params=None` as arguments.
    - Inside the function, call `matplotlib.rcParams.update()` with your new style dictionary.

3. **Expose the New Style in `__init__.py`**:
    - Open `pubstyle/__init__.py`.
    - Import your new function (e.g., `apply_journal_style`) and the style dictionary (e.g., `JOURNAL_STYLE_PARAMS`).
    - Add their names to the `__all__` list to make them part of the public API.

4. **Generate Sample Plots for Documentation**:
    - A crucial step is to provide visual examples of your new style.
    - You can modify `pubstyle/cli.py` or create a temporary script to generate "before" (default matplotlib) and "after" (your new style) plots.
    - Name the images clearly, e.g., `sample_journal_style_plot.png`.

5. **Update the `README.md`**:
    - Add the sample images you generated to the `assets/` directory.
    - Edit `README.md` to add a new section for your style, showing the "before" and "after" images. Use the existing examples as a template.

## Submitting Your Contribution

1. **Create a new branch** for your feature:

    ```bash
    git checkout -b feature/add-journal-style
    ```

2. **Commit your changes** with a clear commit message.
3. **Push your branch** to your fork on GitHub.
4. **Open a Pull Request** to the main `pubstyle` repository.
    - Provide a clear title and description for your pull request, explaining the changes you've made.

Thank you again for your interest in contributing!

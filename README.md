# pubstyle: Publication-Quality Matplotlib Styles

`pubstyle` is a Python package providing a simple way to apply professional, publication-quality styles to your Matplotlib plots. It offers a clean default style and an easy way to enable LaTeX rendering for superior mathematical typesetting.

## Features

- Apply a consistent, paper-ready style with a single function call.
- Optionally enable LaTeX rendering for text and math.
- Customize style parameters easily, either by passing a dictionary or modifying the base configuration.
- Includes a CLI tool to inspect current style settings and generate sample plots.

## Installation

To install `pubstyle`, navigate to the project's root directory (`pubstyle`) in your terminal and run:

```bash
python -m pip install .
```

For development (editable install), use:

```bash
python -m pip install -e .
```

This will also install Matplotlib if it's not already present.

## Basic Usage

### Applying the Default Style

In your Python script, import and call `apply_paper_style` before creating your plots:

```python
import matplotlib.pyplot as plt
from pubstyle import apply_paper_style, reset_to_default_style

# Apply the publication style
apply_paper_style()

plt.figure()
plt.plot([0, 1], [0, 1], label='My Data')
plt.title('My Plot with pubstyle')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.savefig('my_styled_plot.png')

# Optionally, reset to Matplotlib defaults if needed later
# reset_to_default_style()
```

### Enabling LaTeX Rendering

If you have a LaTeX distribution installed (see section below), you can enable LaTeX for all text elements:

```python
apply_paper_style(use_latex=True)
```

This is highly recommended for plots containing mathematical symbols or if you want fonts to perfectly match a LaTeX document.

### Customizing Style Parameters

`pubstyle` comes with a set of default parameters defined in `pubstyle/_style_config.py` (`PAPER_STYLE_PARAMS`). You can override these in two ways:

1. **Passing a custom dictionary to `apply_paper_style`**:

    ```python
    from pubstyle import PAPER_STYLE_PARAMS

    my_customizations = PAPER_STYLE_PARAMS.copy()
    my_customizations.update({
        'font.size': 12,
        'figure.figsize': (8, 6),
        'axes.labelsize': 12,
    })

    apply_paper_style(custom_params=my_customizations)
    ```

2. **Directly modifying `pubstyle/_style_config.py`**:
    If you want to change the default style for all your projects using this installation of `pubstyle`, you can edit the `PAPER_STYLE_PARAMS` dictionary in `pubstyle/_style_config.py` directly.

### Using the Command-Line Interface (CLI)

After installation, `pubstyle` provides a CLI tool named `pubstyle-cli`:

- **Inspect current style configuration**:

    ```bash
    pubstyle-cli
    ```

- **Generate sample plots** (`sample_paper_style_plot.png` and `sample_default_style_plot.png` in the current directory):

    ```bash
    pubstyle-cli --generate-samples
    ```

## Using LaTeX for Text Rendering

Using LaTeX for text rendering in Matplotlib plots ensures high-quality typesetting, especially for mathematical equations, and provides consistency with documents prepared in LaTeX.

To use this feature in `pubstyle`, simply call `apply_paper_style(use_latex=True)`.

**You must have a working LaTeX distribution installed on your system.**

### LaTeX Installation Instructions

Choose the appropriate distribution for your operating system:

#### 1. macOS (Apple Silicon & Intel)

The recommended distribution is **MacTeX**. It's a comprehensive package and works well on both Apple Silicon (M1/M2/M3) and Intel Macs.

- Visit the [MacTeX website](https://www.tug.org/mactex/).
- Download the `MacTeX.pkg` installer (it's a large file).
- Run the installer. This will install LaTeX and related tools like `pdflatex`, `xelatex`, `lualatex`, and the `dvipng` utility (which Matplotlib might use).
- After installation, open a new terminal window. Matplotlib should automatically find the LaTeX installation.

#### 2. Windows

The recommended distribution is **MiKTeX** or **TeX Live**.

- **MiKTeX** ([miktex.org](https://miktex.org/)) is often easier for Windows users as it can install missing packages on-the-fly.
  - Download the MiKTeX installer.
  - Run the installer. Ensure that the installation directory is added to your system's PATH environment variable (usually done by the installer).
- **TeX Live** ([tug.org/texlive/acquire-netinstall.html](https://www.tug.org/texlive/acquire-netinstall.html)) is more comprehensive but has a larger initial download.
  - Follow the instructions for installing TeX Live on Windows.

After installation, you might need to restart your terminal or system for Matplotlib to recognize LaTeX.

#### 3. Linux

The recommended distribution is **TeX Live**. Most Linux distributions offer it through their package managers.

- **Debian/Ubuntu-based systems**:

    ```bash
    sudo apt update
    sudo apt install texlive-full # For a complete installation (large)
    # Or, for a more minimal setup suitable for Matplotlib:
    # sudo apt install texlive-latex-base texlive-latex-extra texlive-fonts-recommended dvipng cm-super
    ```

- **Fedora/RHEL-based systems**:

    ```bash
    sudo dnf install texlive-scheme-full # For a complete installation
    # Or, a more minimal set:
    # sudo dnf install texlive texlive-latex texlive-dvipng texlive-cm-super texlive-collection-fontsrecommended
    ```

- **Arch Linux**:

    ```bash
    sudo pacman -Syu texlive-most
    # Or, for a more minimal setup:
    # sudo pacman -Syu texlive-core texlive-bin texlive-latexextra dvipng
    ```

Ensure `dvipng` is also installed, as Matplotlib often uses it when `text.usetex` is enabled.

#### Verifying LaTeX for Matplotlib

After installing LaTeX, you can test if Matplotlib can find it by running a simple Python script:

```python
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
try:
    plt.figure()
    plt.text(0.5, 0.5, r'Hello $\alpha+\beta=\gamma$ LaTeX!', ha='center')
    plt.savefig('test_latex.png')
    print("LaTeX test successful! Check test_latex.png")
except RuntimeError as e:
    print(f"LaTeX test failed: {e}")
    print("Ensure LaTeX is installed and in your system's PATH.")
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request on the project's repository (link to be added).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details (to be added).

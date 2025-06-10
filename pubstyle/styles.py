import matplotlib as mpl
import matplotlib.pyplot as plt
from ._styles_config import PAPER_STYLE_PARAMS

def apply_paper_style(custom_params=None, use_latex=False):
    """
    Applies a style to Matplotlib for publication-quality plots.
    Uses PAPER_STYLE_PARAMS by default, but can accept a custom dictionary.

    Args:
        custom_params (dict, optional): A dictionary of Matplotlib rcParams
            to override the default PAPER_STYLE_PARAMS.
        use_latex (bool, optional): If True, enables LaTeX for text rendering.
            Defaults to False. Requires a LaTeX installation.
    """
    params_to_apply = PAPER_STYLE_PARAMS.copy() # Start with base style
    message = "Applied default 'paper_style'"

    if custom_params:
        params_to_apply.update(custom_params)
        message = "Applied custom style parameters"

    if use_latex:
        latex_settings = {
            'text.usetex': True,
            'text.latex.preamble': r'\usepackage{amsmath} \usepackage{amssymb}'
        }
        params_to_apply.update(latex_settings)
        message += " with LaTeX rendering enabled"
    
    mpl.rcParams.update(params_to_apply)
    print(f"{message} to Matplotlib.")

def reset_to_default_style():
    """Resets Matplotlib style to its default settings."""
    mpl.rcParams.update(mpl.rcParamsDefault)
    plt.style.use('default') # Ensure any plt.style.use() is also reset
    print("Reset Matplotlib style to default.")

def generate_sample_plots():
    """Generates sample plots using the current style and default style."""
    # You can add test code here, e.g., to print available fonts
    # import matplotlib.font_manager
    # print(sorted(set(f.name for f in matplotlib.font_manager.fontManager.ttflist)))
    
    print("Generating sample plots...")
    # Example of applying the style and creating a dummy plot
    apply_paper_style()
    plt.figure()
    plt.plot([0, 1, 2], [0, 1, 0], label='Sample Data')
    plt.title('Sample Plot with Paper Style')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    # plt.show() # Commented out to prevent GUI pop-up during automated runs
    plt.savefig('sample_paper_style_plot.png')
    print("Saved sample_paper_style_plot.png")
    
    reset_to_default_style()
    plt.figure()
    plt.plot([0, 1, 2], [0, 1, 0], label='Sample Data')
    plt.title('Sample Plot with Default Style')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    # plt.show() # Commented out to prevent GUI pop-up during automated runs
    plt.savefig('sample_default_style_plot.png')
    print("Saved sample_default_style_plot.png")
    print("Sample plot generation finished.")

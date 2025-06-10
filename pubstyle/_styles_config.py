# Default style parameters for publication-quality plots
# You can customize these values as needed.

PAPER_STYLE_PARAMS = {
    # Font settings
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Palatino', 'Computer Modern Roman'],
    # 'font.sans-serif': ['Helvetica', 'Arial'],
    'font.size': 11,              # Base font size

    # Axes settings
    'axes.labelsize': 11,         # Fontsize of the x and y labels
    'axes.titlesize': 12,         # Fontsize of the axes title
    'axes.grid': True,
    'axes.linewidth': 0.8,

    # Tick settings
    'xtick.labelsize': 9,         # Fontsize of the x tick labels
    'ytick.labelsize': 9,         # Fontsize of the y tick labels
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 4,
    'ytick.major.size': 4,
    'xtick.minor.size': 2,
    'ytick.minor.size': 2,

    # Legend settings
    'legend.fontsize': 9,
    'legend.frameon': True,       # Draw a frame around the legend
    'legend.edgecolor': 'black',  # Frame color
    'legend.framealpha': 1,       # Frame transparency
    'legend.fancybox': False,     # Use square corners for the legend box

    # Figure settings
    'figure.figsize': (5, 4),     # Default figure size in inches (width, height)
    'figure.dpi': 300,
    'figure.titlesize': 12,       # Fontsize of the suptitle

    # Line settings
    'lines.linewidth': 1.5,
    'lines.markersize': 5,

    # Grid settings
    'grid.color': 'grey',
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
    'grid.alpha': 0.7,

    # Savefig settings
    'savefig.dpi': 300,
    'savefig.format': 'png',
    'savefig.bbox': 'tight', # May conflict with constrained_layout

    # LaTeX settings (optional)
    # 'text.usetex': True,
    # 'text.latex.preamble': r'\usepackage{amsmath} \usepackage{amssymb}',
}

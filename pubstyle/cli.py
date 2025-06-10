import argparse
import json
from ._styles_config import PAPER_STYLE_PARAMS
from .styles import generate_sample_plots

def main():
    """CLI for publication_styles package."""
    parser = argparse.ArgumentParser(
        description="Manage and inspect publication-quality Matplotlib styles."
    )
    parser.add_argument(
        '--generate-samples',
        action='store_true',
        help="Generate sample plots to visualize the current style."
    )
    # Add other arguments here in the future if needed, e.g., --set-param, --load-style

    args = parser.parse_args()

    if args.generate_samples:
        generate_sample_plots()
    else:
        # Default action: print current style configuration
        print("Current 'paper_style' Matplotlib rcParams configuration:")
        print("=" * 50)
        print(json.dumps(PAPER_STYLE_PARAMS, indent=4))
        print("=" * 50)
        print("These settings are applied when 'apply_paper_style()' is called.")
        print("\nUse --generate-samples to create example plots.")

if __name__ == "__main__":
    main()

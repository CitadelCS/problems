"""
Helper for the Color Codes problem. Do not modify this file.

Usage, in hexcolor.py:

    from swatch import swatch

    swatch(255, 128, 0)   # prints a bar of orange
"""


def swatch(r, g, b, width=20):
    """Print a bar of the color with red r, green g, and blue b (each 0 to 255)."""
    for value in (r, g, b):
        if not isinstance(value, int) or not 0 <= value <= 255:
            raise ValueError("swatch() needs three ints from 0 to 255")
    # \033[48;2;R;G;Bm sets the background color; \033[0m resets it.
    print(f"\033[48;2;{r};{g};{b}m{' ' * width}\033[0m")

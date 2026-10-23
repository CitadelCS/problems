import re

import check50


@check50.check()
def exists():
    """hexcolor.py exists"""
    check50.exists("hexcolor.py")
    check50.include("swatch.py")


def expect(code, color, rgb, complement):
    check50.run("python3 hexcolor.py").stdin(code, prompt=False) \
        .stdout(re.escape(f"Color: {color}"), f"Color: {color}", regex=True) \
        .stdout(re.escape(f"RGB: {rgb}"), f"RGB: {rgb}", regex=True) \
        .stdout(re.escape(f"Complement: {complement}"), f"Complement: {complement}", regex=True) \
        .exit(0)


@check50.check(exists)
def test_orange():
    """input of #FF8000 yields #FF8000, RGB 255 128 0, complement #007FFF"""
    expect("#FF8000", "#FF8000", "255 128 0", "#007FFF")


@check50.check(exists)
def test_no_hash():
    """input of 1E90FF (no #) yields #1E90FF, RGB 30 144 255, complement #E16F00"""
    expect("1E90FF", "#1E90FF", "30 144 255", "#E16F00")


@check50.check(exists)
def test_lowercase():
    """input of #a0b0c0 (lowercase) yields #A0B0C0, RGB 160 176 192, complement #5F4F3F"""
    expect("#a0b0c0", "#A0B0C0", "160 176 192", "#5F4F3F")


@check50.check(exists)
def test_black():
    """input of #000000 yields RGB 0 0 0, complement #FFFFFF"""
    expect("#000000", "#000000", "0 0 0", "#FFFFFF")


@check50.check(exists)
def test_padding():
    """input of #F0FAFF yields RGB 240 250 255, complement #0F0500"""
    expect("#F0FAFF", "#F0FAFF", "240 250 255", "#0F0500")


@check50.check(exists)
def test_swatches():
    """hexcolor.py displays swatches of the color and its complement using swatch()"""
    check50.run("python3 hexcolor.py").stdin("#FF8000", prompt=False) \
        .stdout(re.escape("\033[48;2;255;128;0m"), "swatch of 255 128 0", regex=True) \
        .stdout(re.escape("\033[48;2;0;127;255m"), "swatch of 0 127 255", regex=True) \
        .exit(0)


def rejects(code):
    check50.run("python3 hexcolor.py").stdin(code, prompt=False).reject()


@check50.check(exists)
def test_too_short():
    """input of #FF80 results in reprompt"""
    rejects("#FF80")


@check50.check(exists)
def test_too_long():
    """input of #FF80000 results in reprompt"""
    rejects("#FF80000")


@check50.check(exists)
def test_not_hex():
    """input of #GG0000 results in reprompt"""
    rejects("#GG0000")


@check50.check(exists)
def test_empty():
    """empty input results in reprompt"""
    rejects("")


@check50.check(exists)
def test_prefix():
    """input of 0x12AB results in reprompt"""
    rejects("0x12AB")

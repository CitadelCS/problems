import check50
from pexpect import EOF
from re import escape


@check50.check()
def exists():
    """canteen.py exists"""
    check50.exists("canteen.py")


@check50.check(exists)
def test_EOF():
    """input of EOF halts program"""
    check50.run("python3 canteen.py").stdin(EOF, prompt=False).exit(0)


@check50.check(test_EOF)
def test_basic_order():
    """input of \"taco\", \"taco\", and \"tortilla salad\" results in $20.00"""
    items = ["taco", "taco", "tortilla salad"]
    output = 20.0
    check50.run("python3 canteen.py").stdin(items[0], prompt=True).stdin(
        items[1], prompt=True
    ).stdin(items[2], prompt=True).stdout(
        regex(f"{output:.2f}"), f"${output:.2f}", regex=True
    ).kill()

@check50.check(test_EOF)
def test_basic_order_2():
    """input of \"chicken sandwich\", \"bowl\", and \"nachos\" results in $26.00"""
    items = ["chicken sandwich", "bowl", "nachos"]
    output = 26.0
    check50.run("python3 canteen.py").stdin(items[0], prompt=True).stdin(
        items[1], prompt=True
    ).stdin(items[2], prompt=True).stdout(
        regex(f"{output:.2f}"), f"${output:.2f}", regex=True
    ).kill()


@check50.check(test_EOF)
def test_basic_order_3():
    """input of \"Baja Taco\", \"GriLLed Nuggets\", and \"Super Quesadilla\" results in $22.25"""
    items = ["Baja Taco", "GriLLed Nuggets", "Super Quesadilla"]
    output = 22.25
    check50.run("python3 canteen.py").stdin(items[0], prompt=True).stdin(
        items[1], prompt=True
    ).stdin(items[2], prompt=True).stdout(
        regex(f"{output:.2f}"), f"${output:.2f}", regex=True
    ).kill()


@check50.check(test_EOF)
def test_capitalization():
    """input of \"Super quesadilla\" results in $9.50"""
    input = "Super quesadilla"
    output = 9.50
    check50.run("python3 canteen.py").stdin(input, prompt=True).stdout(
        regex(f"{output:.2f}"), f"${output:.2f}", regex=True
    ).kill()


@check50.check(test_EOF)
def test_invalid_order():
    """input of \"burger\" results in reprompt"""
    input = "burger"
    check50.run("python3 canteen.py").stdin(input, prompt=True).stdout(
        r"(?<!\n)Item: ", "Item: "
    ).kill()


def regex(cost):
    """match case-insensitively with dollar-sign required and only characters on either side"""
    return rf"(?i)^[\D]*\${escape(cost)}[\D]*$"
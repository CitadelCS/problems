import re

import check50


@check50.check()
def exists():
    """ip.py exists"""
    check50.exists("ip.py")


@check50.check(exists)
def no_builtins():
    """ip.py converts to binary without bin() or format()"""
    source = open("ip.py").read()
    if re.search(r"\bbin\s*\(|\bformat\s*\(|:0?\d*b\s*\}", source):
        raise check50.Failure(
            "ip.py appears to use bin(), format(), or a :b format spec",
            help="Write your own function that converts using repeated division by 2",
        )


def run(address, expected):
    check50.run("python3 ip.py").stdin(address, prompt=False).stdout(
        re.escape(expected), expected, regex=True
    ).exit(0)


@check50.check(exists)
def test_home():
    """input of 192.168.0.1 yields 11000000.10101000.00000000.00000001"""
    run("192.168.0.1", "11000000.10101000.00000000.00000001")


@check50.check(exists)
def test_dns():
    """input of 8.8.4.4 yields 00001000.00001000.00000100.00000100"""
    run("8.8.4.4", "00001000.00001000.00000100.00000100")


@check50.check(exists)
def test_extremes():
    """input of 0.127.128.255 yields 00000000.01111111.10000000.11111111"""
    run("0.127.128.255", "00000000.01111111.10000000.11111111")


@check50.check(exists)
def test_whitespace():
    """input of  10.0.0.1  (with surrounding spaces) yields 00001010.00000000.00000000.00000001"""
    run("  10.0.0.1  ", "00001010.00000000.00000000.00000001")


def rejects(address):
    check50.run("python3 ip.py").stdin(address, prompt=False).reject()


@check50.check(exists)
def test_too_big():
    """input of 192.168.0.256 results in reprompt"""
    rejects("192.168.0.256")


@check50.check(exists)
def test_too_few():
    """input of 192.168.0 results in reprompt"""
    rejects("192.168.0")


@check50.check(exists)
def test_too_many():
    """input of 1.2.3.4.5 results in reprompt"""
    rejects("1.2.3.4.5")


@check50.check(exists)
def test_empty_octet():
    """input of 10..0.1 results in reprompt"""
    rejects("10..0.1")


@check50.check(exists)
def test_not_numbers():
    """input of cat.dog.fish.bird results in reprompt"""
    rejects("cat.dog.fish.bird")


@check50.check(exists)
def test_negative():
    """input of 10.-1.0.1 results in reprompt"""
    rejects("10.-1.0.1")

import check50
from re import escape

# adds case insensitivity
case_insensitive_prefix = "(?i)"

@check50.check()
def exists():
    """coke.py exists"""
    check50.exists("coke.py")


@check50.check(exists)
def test_25():
    """coke accepts 25 cents"""
    input = "25"
    output = "Amount Due: 50\n"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(case_insensitive_prefix + output, output, regex=True).kill()


@check50.check(exists)
def test_10():
    """coke accepts 10 cents"""
    input = "10"
    output = "Amount Due: 65\n"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(case_insensitive_prefix + output, output, regex=True).kill()


@check50.check(exists)
def test_1():
    """coke accepts 5 cents"""
    input = "5"
    output = "Amount Due: 70\n"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(case_insensitive_prefix + output, output, regex=True).kill()


@check50.check(exists)
def test_invalid():
    """coke rejects invalid amount of cents"""
    input = "30"
    output = "Amount Due: 75\n"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(case_insensitive_prefix + output, output, regex=True).kill()


@check50.check(exists)
def test_multiple():
    """coke accepts continued input"""
    input = "10"
    output = "Amount Due: 55\n"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdin(input, prompt=True).stdout(case_insensitive_prefix + output, output, regex=True).kill()


@check50.check(exists)
def test_terminate():
    """coke terminates at 75 cents"""
    input = "10"
    output = "Change Owed: 0\n"
    check50.run("python3 coke.py").stdin("25", prompt=True).stdin(input, prompt=True).stdin(input, prompt=True).stdin(input, prompt=True).stdin(input, prompt=True).stdin(input, prompt=True).stdout(case_insensitive_prefix + output, output, regex=True).exit()


@check50.check(exists)
def test_change():
    """coke provides correct change"""
    input = "25"
    output = "Change Owed: 10\n"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdin(input, prompt=True).stdin("10", prompt=True).stdin(input, prompt=True).stdout(case_insensitive_prefix + output, output, regex=True).exit()
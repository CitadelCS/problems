import check50


@check50.check()
def exists():
    """knob.py exists"""
    check50.exists("knob.py")


@check50.check(exists)
def test_1842():
    """input of 1842 yields output of Yes"""
    input = "1842"
    output = "Yes"
    check50.run("python3 knob.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_forty_two():
    """input of eighteen forty-two yields output of Yes"""
    input = "eighteen forty-two"
    output = "Yes"
    check50.run("python3 knob.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_forty_two_space():
    """input of eighteen forty two yields output of Yes"""
    input = "eighteen forty two"
    output = "Yes"
    check50.run("python3 knob.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_forty_two_malformed():
    """input of eiGHtEEn fORty tWo yields output of Yes"""
    input = "eiGHtEEn fORty tWo"
    output = "Yes"
    check50.run("python3 knob.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_1842_spaces():
    """input of 1842, with spaces on either side, yields output of Yes"""
    input = " 1842  "
    output = "Yes"
    check50.run("python3 knob.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_50():
    """input of 50 yields output of No"""
    input = "50"
    output = "No"
    check50.run("python3 knob.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_forty():
    """input of forty yields output of No"""
    input = "forty"
    output = "No"
    check50.run("python3 knob.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(answer):
    """match case-insensitively with only whitespace on either side"""
    return rf'(?i)^\s*{answer}\s*$'
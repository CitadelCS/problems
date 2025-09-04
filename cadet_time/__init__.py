import check50
from re import escape


@check50.check()
def exists():
    """cadet_time.py exists"""
    check50.exists("cadet_time.py")
    check50.include("testing.py")


@check50.check(exists)
def test_times():
    """convert successfully returns decimal hours"""
    tests = {"7:30": 7.5, "14:15": 14.25, "22:00": 22.0}
    for time in tests:
        check50.run("python3 testing.py").stdin(time, prompt=True).stdout(tests[time]).exit()
    

@check50.check(test_times)
def test_pt():
    """input of 5:20 yields output of \"pt time\""""
    input = "5:20"
    output = "pt time"
    check50.run("python3 cadet_time.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(test_times)
def test_pt2():
    """input of 6:30 yields output of \"pt time\""""
    input = "6:30"
    output = "pt time"
    check50.run("python3 cadet_time.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(test_times)
def test_class():
    """input of 11:42 yields output of \"class time\""""
    input = "11:42"
    output = "class time"
    check50.run("python3 cadet_time.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(test_times)
def test_class2():
    """input of 14:00 yields output of \"class time\""""
    input = "14:00"
    output = "class time"
    check50.run("python3 cadet_time.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(test_times)
def test_study():
    """input of 20:32 yields output of \"study time\""""
    input = "20:32"
    output = "study time"
    check50.run("python3 cadet_time.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(test_times)
def test_sleepy():
    """input of 23:32 yields output of \"sleepy time\""""
    input = "23:32"
    output = "sleepy time"
    check50.run("python3 cadet_time.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(test_times)
def test_sleepy2():
    """input of 3:32 yields output of \"sleepy time\""""
    input = "3:32"
    output = "sleepy time"
    check50.run("python3 cadet_time.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(test_times)
def test_no_output():
    """input of 16:15 yields no output"""
    input = "16:15"
    output = ""
    check50.run("python3 cadet_time.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

 
def regex(time):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{escape(time)}\s*$'
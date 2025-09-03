import re
import check50

@check50.check()
def exists():
    """simple_grader.py exists"""
    check50.exists("simple_grader.py")

@check50.check(exists)
def handles_85_of_100():
    """85/100 -> Grade: B, Score: 85.00%"""
    (check50.run("python3 simple_grader.py")
        .stdin("100")
        .stdin("85")
        .stdout(re.compile(r"Grade:\s*B"))
        .stdout(re.compile(r"Score:\s*85\.00%"))
        .exit(0))

@check50.check(exists)
def handles_perfect_score():
    """100/100 -> Grade: A, Score: 100.00%"""
    (check50.run("python3 simple_grader.py")
        .stdin("100")
        .stdin("100")
        .stdout(re.compile(r"Grade:\s*A"))
        .stdout(re.compile(r"Score:\s*100\.00%"))
        .exit(0))

@check50.check(exists)
def handles_zero_score():
    """0/100 -> Grade: F, Score: 0.00%"""
    (check50.run("python3 simple_grader.py")
        .stdin("100")
        .stdin("0")
        .stdout(re.compile(r"Grade:\s*F"))
        .stdout(re.compile(r"Score:\s*0\.00%"))
        .exit(0))

@check50.check(exists)
def handles_boundary_90():
    """90/100 -> Grade: A, Score: 90.00%"""
    (check50.run("python3 simple_grader.py")
        .stdin("100")
        .stdin("90")
        .stdout(re.compile(r"Grade:\s*A"))
        .stdout(re.compile(r"Score:\s*90\.00%"))
        .exit(0))

@check50.check(exists)
def handles_boundary_80():
    """80/100 -> Grade: B, Score: 80.00%"""
    (check50.run("python3 simple_grader.py")
        .stdin("100")
        .stdin("80")
        .stdout(re.compile(r"Grade:\s*B"))
        .stdout(re.compile(r"Score:\s*80\.00%"))
        .exit(0))

@check50.check(exists)
def handles_floats_and_rounding():
    """72.5/80 -> Grade: A, Score: 90.62%"""
    (check50.run("python3 simple_grader.py")
        .stdin("80")
        .stdin("72.5")
        .stdout(re.compile(r"Grade:\s*A"))
        .stdout(re.compile(r"Score:\s*90\.62%"))
        .exit(0))

@check50.check(exists)
def handles_divide_by_zero():
    """total=0 triggers error message"""
    (check50.run("python3 simple_grader.py")
        .stdin("0")
        .stdin("50")
        .stdout(re.compile(r"Error:\s*Total points cannot be zero\."))
        .exit(0))

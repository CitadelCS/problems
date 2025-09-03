import check50
import numbers
import importlib.util

@check50.check()
def exists():
    """simple_grader.py exists"""
    check50.exists("simple_grader.py")

@check50.check(exists)
def has_calc_score():
    """function calc_score exists and returns (percent, letter)"""
    spec = importlib.util.spec_from_file_location("simple_grader", "simple_grader.py")
    simple_grader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(simple_grader)

    assert hasattr(simple_grader, "calc_score"), "calc_score function not found"
    func = getattr(simple_grader, "calc_score")
    assert callable(func), "calc_score is not callable"

    result = func(85, 100)  # try a sample input
    assert isinstance(result, tuple), "calc_score should return a tuple"
    assert len(result) == 2, "calc_score should return a tuple of length 2"
    percent, letter = result
    assert isinstance(percent, numbers.Number), "first element of tuple should be numeric (percent)"
    assert isinstance(letter, str), "second element of tuple should be a string (letter grade)"


@check50.check(exists)
def handles_85_of_100():
    """85/100 -> Grade: B, Score: 85.00%"""
    (check50.run("python3 simple_grader.py")
        .stdin("100")
        .stdin("85")
        .stdout("Grade:\s*B\nScore:\s*85\.00%", regex=True)
        .exit(0))

@check50.check(exists)
def handles_perfect_score():
    """100/100 -> Grade: A, Score: 100.00%"""
    (check50.run("python3 simple_grader.py")
        .stdin("100")
        .stdin("100")
        .stdout("Grade:\s*A\nScore:\s*100\.00%", regex=True)
        .exit(0))

@check50.check(exists)
def handles_zero_score():
    """0/100 -> Grade: F, Score: 0.00%"""
    (check50.run("python3 simple_grader.py")
        .stdin("100")
        .stdin("0")
        .stdout("Grade:\s*F\nScore:\s*0\.00%", regex=True)
        .exit(0))

@check50.check(exists)
def handles_boundary_90():
    """90/100 -> Grade: A, Score: 90.00%"""
    (check50.run("python3 simple_grader.py")
        .stdin("100")
        .stdin("90")
        .stdout("Grade:\s*A\nScore:\s*90\.00%", regex=True)
        .exit(0))

@check50.check(exists)
def handles_boundary_80():
    """80/100 -> Grade: B, Score: 80.00%"""
    (check50.run("python3 simple_grader.py")
        .stdin("100")
        .stdin("80")
        .stdout("Grade:\s*B\nScore:\s*80\.00%", regex=True)
        .exit(0))

@check50.check(exists)
def handles_floats_and_rounding():
    """72.5/80 -> Grade: A, Score: 90.62%"""
    (check50.run("python3 simple_grader.py")
        .stdin("80")
        .stdin("72.5")
        .stdout("Grade:\s*A\nScore:\s*90\.62%", regex=True)
        .exit(0))

@check50.check(exists)
def handles_divide_by_zero():
    """total=0 triggers error message"""
    (check50.run("python3 simple_grader.py")
        .stdin("0")
        .stdin("50")
        .stdout("Error:\s*Total points cannot be zero\.", regex=True)
        .exit(0))

@check50.check(exists)
def handles_negative():
    """total=-24 triggers error message"""
    (check50.run("python3 simple_grader.py")
        .stdin("-24")
        .stdin("50")
        .stdout("Error:\s*Total points cannot be negative\.", regex=True)
        .exit(0))

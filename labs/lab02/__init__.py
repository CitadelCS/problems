import check50
import importlib.util
import numbers

@check50.check()
def exists():
    """fuel_efficiency.py exists"""
    check50.exists("fuel_efficiency.py")

@check50.check(exists)
def has_calc_efficiency():
    """function calc_efficiency exists and returns (mpg, label)"""
    spec = importlib.util.spec_from_file_location("fuel_efficiency", "fuel_efficiency.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert hasattr(mod, "calc_efficiency"), "calc_efficiency function not found"
    func = getattr(mod, "calc_efficiency")
    assert callable(func), "calc_efficiency is not callable"

    mpg, label = func(120, 4)  # 30 MPG → "Good" (just sanity-check the shape/types)
    assert isinstance(mpg, numbers.Number), "first element should be numeric (mpg)"
    assert isinstance(label, str), "second element should be a string (label)"

@check50.check(exists)
def handles_typical_average():
    """300 miles, 12 gal -> Average, 25.00 MPG"""
    (check50.run("python3 fuel_efficiency.py")
        .stdin("300")
        .stdin("12")
        .stdout("Efficiency:\s*Average\nMPG:\s*25\.00", regex=True)
        .exit(0))

@check50.check(exists)
def handles_good_boundary():
    """120 miles, 4 gal -> Good, 30.00 MPG"""
    (check50.run("python3 fuel_efficiency.py")
        .stdin("120")
        .stdin("4")
        .stdout("Efficiency:\s*Good\nMPG:\s*30\.00", regex=True)
        .exit(0))

@check50.check(exists)
def handles_excellent_boundary():
    """200 miles, 5 gal -> Excellent, 40.00 MPG"""
    (check50.run("python3 fuel_efficiency.py")
        .stdin("200")
        .stdin("5")
        .stdout("Efficiency:\s*Excellent\nMPG:\s*40\.00", regex=True)
        .exit(0))

@check50.check(exists)
def handles_poor_case():
    """50 miles, 3 gal -> Poor, 16.67 MPG"""
    (check50.run("python3 fuel_efficiency.py")
        .stdin("50")
        .stdin("3")
        .stdout("Efficiency:\s*Poor\nMPG:\s*16\.67", regex=True)
        .exit(0))

@check50.check(exists)
def handles_rounding():
    """145 miles, 4 gal -> Good, 36.25 MPG"""
    (check50.run("python3 fuel_efficiency.py")
        .stdin("145")
        .stdin("4")
        .stdout("Efficiency:\s*Good\nMPG:\s*36\.25", regex=True)
        .exit(0))

@check50.check(exists)
def divide_by_zero():
    """gallons=0 prints error"""
    (check50.run("python3 fuel_efficiency.py")
        .stdin("100")
        .stdin("0")
        .stdout("Error:\s*Gallons used cannot be zero\.", regex=True)
        .exit(0))

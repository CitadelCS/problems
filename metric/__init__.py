import check50

@check50.check()
def exists():
    """metric.py exists"""
    check50.exists("metric.py")

@check50.check()
def whole_number():
    """whole number"""
    check50.run("python3 metric.py").stdin("123", prompt=False).stdout("123.0 feet is 37.49 meters\n123.0 meters is 403.54 feet\n", regex=False).exit(0)

@check50.check()
def exact_conversion_factor():
    """exact conversion factor"""
    check50.run("python3 metric.py").stdin("3048", prompt=False).stdout("3048.0 feet is 929.03 meters\n3048.0 meters is 10000.00 feet\n", regex=False).exit(0)

@check50.check()
def fractional_number():
    """fractional number"""
    check50.run("python3 metric.py").stdin("123.456", prompt=False).stdout("123.456 feet is 37.63 meters\n123.456 meters is 405.04 feet\n", regex=False).exit(0)
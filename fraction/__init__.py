import check50

@check50.check()
def input_of_45_over_46_prints_proper():
    """input of 45 over 46 prints proper"""
    check50.run("python3 fraction.py").stdin("45/46", prompt=True).stdout("proper", regex=False).exit(0)

@check50.check()
def input_of_45_over_15_prints_improper():
    """input of 45 over 15 prints improper"""
    check50.run("python3 fraction.py").stdin("45/15", prompt=True).stdout("improper: 3", regex=False).exit(0)

@check50.check()
def input_of_45_over_25_prints_improper():
    """input of 45 over 25 prints improper"""
    check50.run("python3 fraction.py").stdin("45/25", prompt=True).stdout("improper: 1 + 20/25", regex=False).exit(0)

@check50.check()
def zero_denominator_prints_invalid():
    """zero denominator prints invalid"""
    check50.run("python3 fraction.py").stdin("45/0", prompt=True).stdout("invalid", regex=False).exit(0)
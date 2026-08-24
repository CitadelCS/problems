import check50

# ── Problem 1: Type Error ────────────────────────────────────────────────────

@check50.check()
def problem1_exists():
    """problem1.py exists"""
    check50.exists("problem1.py")

@check50.check(problem1_exists)
def problem1_correct():
    """problem1: next-year calculation is correct"""
    check50.run("python3 problem1.py").stdin("20", prompt=True).stdout("21", regex=True).exit(0)


# ── Problem 2: Syntax Error ──────────────────────────────────────────────────

@check50.check()
def problem2_exists():
    """problem2.py exists"""
    check50.exists("problem2.py")

@check50.check(problem2_exists)
def problem2_correct():
    """problem2: program runs without syntax error"""
    check50.run("python3 problem2.py").stdout("Not an A.", regex=True).exit(0)


# ── Problem 3: Indentation Error ─────────────────────────────────────────────

@check50.check()
def problem3_exists():
    """problem3.py exists"""
    check50.exists("problem3.py")

@check50.check(problem3_exists)
def problem3_correct():
    """problem3: program runs without indentation error"""
    check50.run("python3 problem3.py").stdout("done", regex=True).exit(0)


# ── Problem 4: Off-by-One Error ──────────────────────────────────────────────

@check50.check()
def problem4_exists():
    """problem4.py exists"""
    check50.exists("problem4.py")

@check50.check(problem4_exists)
def problem4_correct():
    """problem4: all five numbers are printed (starting from 10)"""
    check50.run("python3 problem4.py").stdout("10", regex=True).exit(0)


# ── Problem 5: Name Error ────────────────────────────────────────────────────

@check50.check()
def problem5_exists():
    """problem5.py exists"""
    check50.exists("problem5.py")

@check50.check(problem5_exists)
def problem5_correct():
    """problem5: prints correct welcome message"""
    check50.run("python3 problem5.py").stdout("Welcome, Mike", regex=True).exit(0)


# ── Problem 6: TDD ───────────────────────────────────────────────────────────

@check50.check()
def problem6_exists():
    """problem6.py exists"""
    check50.exists("problem6.py")

@check50.check(problem6_exists)
def problem6_welcome():
    """problem6: prints 'Welcome to CSCI 201'"""
    check50.run("python3 problem6.py").stdout("Welcome to CSCI 201", regex=False).exit(0)

@check50.check(problem6_exists)
def problem6_motto():
    """problem6: prints 'Honor, Duty, State, and Country'"""
    check50.run("python3 problem6.py").stdout("Honor, Duty, State, and Country", regex=False).exit(0)

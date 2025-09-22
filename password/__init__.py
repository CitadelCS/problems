import check50

@check50.check()
def exists():
    """password.py exists"""
    check50.exists("password.py")

@check50.check()
def cannot_start_with_a_digit():
    """cannot start with a digit"""
    check50.run("python3 password.py").stdin("1abcDEF!", prompt=False).stdout("invalid", regex=False).exit(0)

@check50.check()
def cannot_be_nine_characters():
    """cannot be nine characters"""
    check50.run("python3 password.py").stdin("aaaBBB!34", prompt=False).stdout("invalid", regex=False).exit(0)

@check50.check()
def cannot_be_seven_characters():
    """cannot be seven characters"""
    check50.run("python3 password.py").stdin("abcDE1!", prompt=False).stdout("invalid", regex=False).exit(0)

@check50.check()
def must_have_one_uppercase_letter():
    """must have one uppercase letter"""
    check50.run("python3 password.py").stdin("abcdef!1", prompt=False).stdout("invalid", regex=False).exit(0)

@check50.check()
def must_have_one_lowercase_letter():
    """must have one lowercase letter"""
    check50.run("python3 password.py").stdin("ABCDEF!1", prompt=False).stdout("invalid", regex=False).exit(0)

@check50.check()
def must_have_one_digit():
    """must have one digit"""
    check50.run("python3 password.py").stdin("ABCdef!!", prompt=False).stdout("invalid", regex=False).exit(0)

@check50.check()
def must_have_one_approved_symbol():
    """must have one approved symbol"""
    check50.run("python3 password.py").stdin("ABCdef&1", prompt=False).stdout("invalid", regex=False).exit(0)

@check50.check()
def must_approve_valid_password1():
    """must approve valid password1"""
    check50.run("python3 password.py").stdin("ABCdef1!", prompt=False).stdout("valid", regex=False).exit(0)

@check50.check()
def must_approve_valid_password2():
    """must approve valid password2"""
    check50.run("python3 password.py").stdin("ABC22f1*", prompt=False).stdout("valid", regex=False).exit(0)

@check50.check()
def must_approve_valid_password3():
    """must approve valid password3"""
    check50.run("python3 password.py").stdin("def2?ABC", prompt=False).stdout("valid", regex=False).exit(0)
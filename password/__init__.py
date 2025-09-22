import check50

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
def must_approve_valid_password():
    """must approve valid password"""
    check50.run("python3 password.py").stdin("def2?ABC", prompt=False).stdout("valid", regex=False).exit(0)
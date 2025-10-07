import check50
import re
import subprocess
import importlib.util
import builtins

@check50.check()
def exists():
    """calculator.py exists"""
    check50.exists("calculator.py")


import check50
import re

import check50
import re

@check50.check(exists)
def check_main_guard():
    """main() is called inside if __name__ == '__main__' block"""
    with open("calculator.py") as f:
        lines = f.readlines()

    # Find the if __name__ == "__main__" guard line
    main_guard_line_nums = [i for i, line in enumerate(lines)
                           if re.match(r'\s*if\s+__name__\s*==\s*[\'"]__main__[\'"]\s*:', line)]
    if not main_guard_line_nums:
        raise check50.Failure("Missing if __name__ == '__main__': guard")

    guard_line_num = main_guard_line_nums[0]

    def is_comment_line(line):
        return bool(re.match(r'^\s*#', line))

    # Find all lines that call main() but exclude function definitions and comment lines
    main_call_line_nums = [i for i, line in enumerate(lines)
                          if (not is_comment_line(line))
                          and re.search(r'\bmain\s*\(\s*\)', line)
                          and not re.match(r'\s*def\s+main\s*\(', line)]

    if not main_call_line_nums:
        raise check50.Failure("No call to main() found")

    # All main() calls should be after the guard line
    for num in main_call_line_nums:
        if num <= guard_line_num:
            raise check50.Failure("main() must be called inside the if __name__ == '__main__': block")

        # Check indentation of main() call > indentation of guard
        guard_indent = len(lines[guard_line_num]) - len(lines[guard_line_num].lstrip())
        main_indent = len(lines[num]) - len(lines[num].lstrip())
        if main_indent <= guard_indent:
            raise check50.Failure("main() call must be indented inside the if __name__ == '__main__': block")


@check50.check(exists)
def check_quit_immediately():
    """Entering 5 immediately quits with 'Goodbye!'"""
    (check50.run("python3 calculator.py")
        .stdin("5")
        .stdout("Goodbye!", regex=True)
        .exit(0))


@check50.check(check_main_guard)
def check_get_number():
    """function get_number exists and handles input properly"""
    spec = importlib.util.spec_from_file_location("calculator", "calculator.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert hasattr(mod, "get_number"), "get_number function not found"
    func = getattr(mod, "get_number")
    assert callable(func), "get_number is not callable"

    # We need to simulate input for get_number. We'll patch 'input' to return values.
    inputs = iter(["notanumber", "42"])

    def fake_input(prompt):
        return next(inputs)

    original_input = builtins.input
    builtins.input = fake_input
    try:
        number = func("Enter a number: ")
        assert isinstance(number, float), "get_number should return a float"
        assert number == 42.0, "get_number should return the valid numeric input"
    finally:
        builtins.input = original_input


@check50.check(exists)
def check_addition():
    """handles addition correctly"""
    (check50.run("python3 calculator.py")
     .stdin("1")
     .stdin("4")
     .stdin("5")
     .stdout("Result:\\s*9\\.0", regex=True)
     .stdin("5")
     .stdout("Goodbye!", regex=True)
     .exit(0))


@check50.check(exists)
def check_invalid_input():
    """handles non-numeric input"""
    (check50.run("python3 calculator.py")
     .stdin("2")
     .stdin("ten")
     .stdout("Error: Please enter a valid number\\.", regex=True)
     .stdin("3")
     .stdin("2")
     .stdin("5")
     .stdout("Goodbye!", regex=True)
     .exit(0))


@check50.check(exists)
def check_divide_by_zero():
    """handles division by zero"""
    (check50.run("python3 calculator.py")
     .stdin("4")
     .stdin("10")
     .stdin("0")
     .stdout("Error: Cannot divide by zero\\.", regex=True)
     .stdin("5")
     .stdout("Goodbye!", regex=True)
     .exit(0))


@check50.check(exists)
def check_try_except_count():
    """uses at least 2 try blocks and 3 except blocks"""
    try_count = int(subprocess.run(
        "grep -c 'try' calculator.py", shell=True, capture_output=True, text=True).stdout.strip())

    except_count = int(subprocess.run(
        "grep -c 'except' calculator.py", shell=True, capture_output=True, text=True).stdout.strip())

    assert try_count >= 2, "Less than 2 try blocks found"
    assert except_count >= 3, "Less than 3 except blocks found"

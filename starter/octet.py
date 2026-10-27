# Exercise 3: Is it an octet?
#
# is_octet(s) returns True if the string s is a whole number from 0 to 255,
# written with digits only, and False otherwise.
#
# Run the program to test your function. Every line should say PASS.


def is_octet(s):
    ...


def main():
    tests = [
        ("0", True),
        ("192", True),
        ("255", True),
        ("256", False),
        ("1000", False),
        ("", False),
        ("-1", False),
        ("1a", False),
        ("cat", False),
        (" 7", False),
    ]
    for s, expected in tests:
        check(f'is_octet("{s}")', is_octet(s), expected)


def check(label, got, expected):
    if got == expected:
        print(f"  PASS {label} is {expected!r}")
    else:
        print(f"  FAIL {label} should be {expected!r}, not {got!r}")


main()

# Exercise 2: Building the binary string
#
# Part A: to_binary(n) returns n in binary as a string, with no extra zeros.
#         Use the repeated division from Exercise 1. Each remainder is the
#         next bit from the RIGHT, so put each new bit in front of the others.
#
# Part B: pad(bits, width) returns bits with zeros added on the left until
#         it is width characters long. pad("101", 8) returns "00000101".
#
# Run the program to test your functions. Every line should say PASS.


def to_binary(n):
    ...


def pad(bits, width):
    ...


def main():
    print("Part A")
    for n, expected in [(1, "1"), (2, "10"), (5, "101"), (41, "101001"), (255, "11111111"), (0, "0")]:
        check(f"to_binary({n})", to_binary(n), expected)

    print("Part B")
    for bits, width, expected in [("101", 8, "00000101"), ("11111111", 8, "11111111"), ("0", 4, "0000")]:
        check(f'pad("{bits}", {width})', pad(bits, width), expected)

    print("Every number from 0 to 255")
    wrong = 0
    for n in range(256):
        # bin(n) returns a string like "0b101", so [2:] skips the "0b"
        if to_binary(n) != bin(n)[2:]:
            wrong += 1
    check("numbers that don't match bin()", wrong, 0)


def check(label, got, expected):
    if got == expected:
        print(f"  PASS {label} is {expected!r}")
    else:
        print(f"  FAIL {label} should be {expected!r}, not {got!r}")


main()

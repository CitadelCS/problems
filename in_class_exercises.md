# In-Class Exercises: Number Systems in Python

These short programs build the pieces you'll need for the problem set. Exercises 2 and 3 include tests: run the program, and when every line says `PASS`, you're done. Work with a partner, and ask for help as soon as you're stuck.

For each exercise, create the file, paste in the starter code, and fill in the `TODO`s and `...`s.

## Exercise 1: Repeated Division

In class you converted 41 to binary by hand by dividing by 2 over and over and writing down the remainders. Now make Python do it.

Implement `remainders.py` so it prints every step. Then try 26, 255, and 1.

**Discuss:** Read the remainders for 41 from the bottom up. What number is that? Why bottom up?

```
mkdir remainders
cd remainders
code remainders.py
```

```python
# Exercise 1: Repeated division
# Prompt for a whole number n, then show each step of dividing by 2
# until the quotient is 0. For 41, the output should be:
#
#   41 // 2 = 20 remainder 1
#   20 // 2 = 10 remainder 0
#   10 // 2 = 5 remainder 0
#   5 // 2 = 2 remainder 1
#   2 // 2 = 1 remainder 0
#   1 // 2 = 0 remainder 1


def main():
    n = int(input("n: "))
    # TODO: loop while n is greater than 0
    #   compute the quotient with // and the remainder with %
    #   print the step
    #   update n


main()
```

## Exercise 2: Building the Binary String

Turn your loop from Exercise 1 into a function that **returns** the binary string instead of printing steps. Then write a second function that pads a binary string with leading zeros.

The last test compares your function against Python's built-in `bin()` for every number from 0 to 255. (`bin()` is fine here for checking your work, but not in your problem set.)

**Discuss:** What did your function return for 0 the first time you ran it? Why?

```
mkdir binary
cd binary
code binary.py
```

```python
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
```

## Exercise 3: Is It an Octet?

Each part of an IP address must be a whole number from 0 to 255. Write a function that decides whether a string qualifies.

**Discuss:** Why does `"-1"` fail even though -1 is less than 255? What would `int(" 7")` do?

```
mkdir octet
cd octet
code octet.py
```

```python
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
```

## Exercise 4: Byte Explorer

Every character has a number, and every number up to 255 fits in one byte. Print the byte behind each character of a command-line argument.

Try `python bytes.py Hi!`, `python bytes.py 'Go Dogs'`, and `python bytes.py` with no argument. What's the number for a space?

```
mkdir bytes
cd bytes
code bytes.py
```

```python
# Exercise 4: Byte explorer
#
# Usage: python bytes.py TEXT
#
# Print one line per character of TEXT: the character, its number,
# and its number as 8 bits. For python bytes.py Hi! the output should be:
#
#   H 72 01001000
#   i 105 01101001
#   ! 33 00100001
#
# If the user doesn't give exactly one argument, exit with a usage message.

import sys


def main():
    # TODO: check len(sys.argv), and sys.exit("Usage: python bytes.py TEXT") if it's wrong
    # TODO: for each character c in sys.argv[1], print c, ord(c), and ord(c) as 8 bits
    #       Hint: f"{n:08b}" formats n as binary, padded with zeros to 8 digits
    ...


main()
```

## Exercise 5: Is It Binary? (if time)

Go the other way: turn 8 bits back into a number and a character, and use `try` and `except` to handle input that isn't binary.

```
mkdir bits
cd bits
code bits.py
```

```python
# Exercise 5: Is it binary?
#
# Prompt the user for a string of bits until they type one that int(s, 2)
# accepts, then print its value in decimal and the character it stands for.
#
#   Bits: 0100100
#   Bits: 01001002
#   Not binary, try again
#   Bits: 01001000
#   72 H
#
# Recall that int(s, 2) raises a ValueError if s isn't valid binary.
# Also reject anything that isn't exactly 8 characters long, as in the first try above.


def main():
    while True:
        s = input("Bits: ")
        # TODO: if s isn't 8 characters long, go back to the top of the loop
        # TODO: try to convert s with int(s, 2) and break out of the loop
        #       if that raises a ValueError, print "Not binary, try again"
        ...
    # TODO: print the number and chr() of the number
    ...


main()
```

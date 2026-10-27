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

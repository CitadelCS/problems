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

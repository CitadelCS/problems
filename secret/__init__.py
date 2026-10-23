import re

import check50


@check50.check()
def exists():
    """secret.py exists"""
    check50.exists("secret.py")


def out(args, expected):
    check50.run(f"python3 secret.py {args}").stdout(
        re.escape(expected), expected, regex=True
    ).exit(0)


def fails(args):
    check50.run(f"python3 secret.py {args}").exit(1)


@check50.check(exists)
def test_encode_hi():
    """python3 secret.py encode Hi yields 01001000 01101001"""
    out("encode Hi", "01001000 01101001")


@check50.check(exists)
def test_encode_words():
    """python3 secret.py encode Go Dogs yields 01000111 01101111 00100000 01000100 01101111 01100111 01110011"""
    out("encode Go Dogs", "01000111 01101111 00100000 01000100 01101111 01100111 01110011")


@check50.check(exists)
def test_encode_punctuation():
    """python3 secret.py encode 'A1!' yields 01000001 00110001 00100001"""
    out("encode 'A1!'", "01000001 00110001 00100001")


@check50.check(exists)
def test_decode_hi():
    """python3 secret.py decode 01001000 01101001 yields Hi"""
    out("decode 01001000 01101001", "Hi")


@check50.check(exists)
def test_decode_space():
    """python3 secret.py decode 01001111 01001011 00100000 00111111 yields OK ?"""
    out("decode 01001111 01001011 00100000 00111111", "OK ?")


@check50.check(exists)
def test_round_trip():
    """decoding the output of encode returns the original text"""
    text = "Bits are bits"
    encoded = check50.run(f"python3 secret.py encode {text}").stdout()
    encoded = encoded.strip()
    out(f"decode {encoded}", text)


@check50.check(exists)
def test_no_args():
    """python3 secret.py exits with code 1"""
    fails("")


@check50.check(exists)
def test_mode_only():
    """python3 secret.py encode exits with code 1"""
    fails("encode")


@check50.check(exists)
def test_bad_mode():
    """python3 secret.py shout Hi exits with code 1"""
    fails("shout Hi")


@check50.check(exists)
def test_not_binary():
    """python3 secret.py decode 01001000 01101002 exits with code 1"""
    fails("decode 01001000 01101002")


@check50.check(exists)
def test_wrong_length():
    """python3 secret.py decode 0100100 exits with code 1"""
    fails("decode 0100100")


@check50.check(exists)
def test_too_big():
    """python3 secret.py encode with an emoji exits with code 1"""
    fails("encode '\U0001F600'")

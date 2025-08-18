import check50

@check50.check()
def cadet_lower():
    """cadet lower"""
    check50.run("python3 honor.py").stdin("cadet", prompt=False).stdout("A CADET DOES NOT LIE, CHEAT,\nOR STEAL,\nNOR TOLERATE THOSE WHO DO.\n", regex=False).exit(0)

@check50.check()
def student_lower():
    """student lower"""
    check50.run("python3 honor.py").stdin("student", prompt=False).stdout("A STUDENT DOES NOT LIE, CHEAT,\nOR STEAL,\nNOR TOLERATE THOSE WHO DO.\n", regex=False).exit(0)

@check50.check()
def cadet_mixed():
    """cadet mixed"""
    check50.run("python3 honor.py").stdin("cAdEt", prompt=False).stdout("A CADET DOES NOT LIE, CHEAT,\nOR STEAL,\nNOR TOLERATE THOSE WHO DO.\n", regex=False).exit(0)

@check50.check()
def any_words():
    """any words"""
    check50.run("python3 honor.py").stdin("golden retriever!", prompt=False).stdout("A GOLDEN RETRIEVER! DOES NOT LIE, CHEAT,\nOR STEAL,\nNOR TOLERATE THOSE WHO DO.\n", regex=False).exit(0)
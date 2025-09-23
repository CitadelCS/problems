import check50
import importlib.util

@check50.check()
def exists():
    """library.py exists"""
    check50.exists("library.py")

@check50.check(exists)
def has_add_book():
    """function add_book exists and mutates the list (returns nothing)"""
    spec = importlib.util.spec_from_file_location("library", "library.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert hasattr(mod, "add_book"), "add_book function not found"
    fn = getattr(mod, "add_book")

    # Prepare an empty library and call function
    lib = []
    result = fn(lib, "Dune", "Frank Herbert")

    # Should return None for now
    assert result is None, "add_book should not return a value yet (should return None)"

    # Library should now contain one dictionary with the right keys/values
    assert isinstance(lib, list), "library should be a list"
    assert len(lib) == 1, "library should have exactly one book after add_book is called"
    book = lib[0]
    assert isinstance(book, dict), "each book should be a dictionary"
    assert book.get("title") == "Dune", 'book["title"] should be "Dune"'
    assert book.get("author") == "Frank Herbert", 'book["author"] should be "Frank Herbert"'

@check50.check(exists)
def add_one_book_then_quit():
    """add 1 book then quit -> prints numbered list with that book"""
    (check50.run("python3 library.py")
        .stdin("yes")
        .stdin("The Hobbit")
        .stdin("J.R.R. Tolkien")
        .stdin("no")
        .stdout("(?s)Your Library:\\s*1\\. \"The Hobbit\" by J\\.R\\.R\\. Tolkien", regex=True)
        .exit(0))

@check50.check(exists)
def add_two_books_then_quit():
    """add 2 books then quit -> prints both in order"""
    (check50.run("python3 library.py")
        .stdin("yes")
        .stdin("The Hobbit")
        .stdin("J.R.R. Tolkien")
        .stdin("yes")
        .stdin("Dune")
        .stdin("Frank Herbert")
        .stdin("no")
        .stdout("\\nYour Library:.*1\\. \"The Hobbit\" by J\\.R\\.R\\. Tolkien.*2\\. \"Dune\" by Frank Herbert", regex=True)
        .exit(0))

@check50.check(exists)
def invalid_choice_message():
    """invalid choice prints prompt then allows quitting"""
    (check50.run("python3 library.py")
        .stdin("maybe")
        .stdout("Please type 'yes' or 'no'\.", regex=True)
        .stdin("no")
        .stdout("\\n*Your Library:", regex=True)
        .exit(0))

@check50.check(exists)
def quits_immediately_prints_header():
    """no immediately -> prints header (no numbered items required)"""
    (check50.run("python3 library.py")
        .stdin("no")
        .stdout("Your Library:", regex=True)
        .exit(0))

@check50.check(exists)
def case_insensitive_yes_no():
    """handles YES/NO in different cases"""
    (check50.run("python3 library.py")
        .stdin("Yes")
        .stdin("Dune")
        .stdin("Frank Herbert")
        .stdin("NO")
        .stdout("\\nYour Library:\\s*1\\. \"Dune\" by Frank Herbert", regex=True)
        .exit(0))

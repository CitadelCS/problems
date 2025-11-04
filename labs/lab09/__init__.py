import importlib.util
import os

import check50

FILENAME = "library_save.py"
TEST_FILE = "test_library.csv"


@check50.check()
def exists():
    """library_save.py exists"""
    check50.exists(FILENAME)


@check50.check(exists)
def has_add_book_and_isbn_logic():
    """add_book exists, adds isbn, prevents duplicates, returns True/False"""
    spec = importlib.util.spec_from_file_location("library", FILENAME)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert hasattr(mod, "add_book"), "add_book function not found"
    fn = getattr(mod, "add_book")

    lib = []

    # First add should succeed
    result1 = fn(lib, "Dune", "Frank Herbert", "9780441172719")
    assert result1 is True, "add_book should return True when adding a new ISBN"
    assert len(lib) == 1, "library should have 1 book after first add"
    assert isinstance(lib[0], dict), "each item in library should be a dictionary"
    assert lib[0].get("isbn") == "9780441172719", "book dictionary should contain the 'isbn' key/value"

    # Duplicate ISBN should fail and not add
    result2 = fn(lib, "Another Dune", "Someone Else", "9780441172719")
    assert result2 is False, "add_book should return False when ISBN already exists"
    assert len(lib) == 1, "library size should remain 1 after duplicate attempt"


@check50.check(exists)
def load_and_save_functions_work():
    """load_library and save_library functions read/write books correctly"""
    # Import library module
    spec = importlib.util.spec_from_file_location("library", FILENAME)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # Ensure functions exist
    assert hasattr(mod, "load_library"), "load_library not found"
    assert hasattr(mod, "save_library"), "save_library not found"

    books = [{"title": "Dune", "author": "Frank Herbert", "isbn": "9780441172719"},
        {"title": "1984", "author": "George Orwell", "isbn": "9780451524935"}, ]

    # Save to file
    mod.save_library(TEST_FILE, books)

    # Now load from file
    loaded = mod.load_library(TEST_FILE)

    assert len(loaded) == 2, "Should load 2 books from file"
    assert loaded[0]["title"] == "Dune", "First book title should be 'Dune'"
    assert loaded[1]["isbn"] == "9780451524935", "Second book ISBN should match"

    # Cleanup
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


@check50.check(exists)
def file_not_found_handled_gracefully():
    """load_library returns empty list when file doesn't exist"""
    spec = importlib.util.spec_from_file_location("library", FILENAME)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert hasattr(mod, "load_library"), "load_library not found"

    result = mod.load_library("nonexistent_file.txt")
    assert isinstance(result, list), "Should return a list"
    assert len(result) == 0, "Should return empty list if file doesn't exist"


@check50.check(exists)
def add_one_book_then_quit():
    """interactive: add 1 book then quit; prints the book with ISBN"""
    (check50.run(f"python3 {FILENAME}").stdin("").stdin("yes").stdin("The Hobbit").stdin("J.R.R. Tolkien").stdin(
        "9780547928227").stdin("no").stdin("no").stdout(
        r'(?s)Your Library:\s*1\. "The Hobbit" by J\.R\.R\. Tolkien \(ISBN: 9780547928227\)', regex=True).exit(0))


@check50.check(exists)
def add_two_books_then_quit():
    """interactive: add 2 distinct books then quit; prints both in order with ISBNs"""
    (check50.run(f"python3 {FILENAME}").stdin("").stdin("yes").stdin("The Hobbit").stdin("J.R.R. Tolkien").stdin(
        "9780547928227").stdin("yes").stdin("Dune").stdin("Frank Herbert").stdin("9780441172719").stdin("no").stdin(
        "no").stdout(
        r'(?s)Your Library:.*1\. "The Hobbit" by J\.R\.R\. Tolkien \(ISBN: 9780547928227\).*2\. "Dune" by Frank Herbert \(ISBN: 9780441172719\)',
        regex=True).exit(0))


@check50.check(exists)
def duplicate_isbn_message():
    """interactive: adding the same ISBN twice prints a duplicate warning"""
    (check50.run(f"python3 {FILENAME}").stdin("").stdin("yes").stdin("Dune").stdin("Frank Herbert").stdin(
        "9780441172719").stdin("yes").stdin("Another Dune").stdin("Someone Else").stdin("9780441172719").stdout(
        r"Book with this ISBN already exists\. Not added to the library\.", regex=True).stdin("no").stdin("no").stdout(
        r".*Your Library:", regex=True).exit(0))


@check50.check(exists)
def invalid_choice_message():
    """interactive: invalid choice prints prompt then allows quitting"""
    (check50.run(f"python3 {FILENAME}").stdin("").stdin("maybe").stdout(r"Please type 'yes' or 'no'\.").stdin(
        "no").stdin("no").stdout(r"\n\s*Your Library:", regex=True).exit(0))


@check50.check(exists)
def quits_immediately_prints_header():
    """interactive: 'no' immediately -> prints header (no numbered items required)"""
    (check50.run(f"python3 {FILENAME}").stdin("").stdin("no").stdin("no").stdout(r"Your Library:", regex=True).exit(0))


@check50.check(exists)
def case_insensitive_yes_no():
    """interactive: handles YES/NO in different cases"""
    (check50.run(f"python3 {FILENAME}").stdin("").stdin("Yes").stdin("Dune").stdin("Frank Herbert").stdin(
        "9780441172719").stdin("NO").stdin("no").stdout(
        r'(?s)Your Library:\s*1\. "Dune" by Frank Herbert \(ISBN: 9780441172719\)', regex=True).exit(0))

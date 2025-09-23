# LAB04 — Simple Library Manager (Part 2: ISBN & Duplicates)

## **Step 1: The Problem**

Create a new Python file called **`library.py`**.

At the **very top of your file**, include a comment with **your name and CWID** like this:

```python
# Name: Jane Doe
# CWID: 12345678
```

In this assignment you will continue modeling a **library** using Python data structures:

- A **book** is a **dictionary** with keys:
  - `"title"` → string  
  - `"author"` → string  
  - `"isbn"` → string (unique identifier)
- The **library** is a **list** of book dictionaries.

Your program should:

1. Start with an **empty library** (empty list).
2. Write a function **`add_book(library, title, author, isbn)`** that:
   - Checks if **`isbn`** is already in the library.
   - If it **exists**, **do not** add the book and **return `False`**.
   - If it **does not exist**, create the dictionary and **append** it to the library, then **return `True`**.
3. Use a **loop** to repeatedly ask the user whether they want to **add a new book** or **quit**.
4. When the user chooses to **add** a book:
   - Prompt for the **title**, **author**, and **ISBN**.
   - Call your **`add_book`** function.
   - If `add_book` returns `False`, print:
     ```
     Book with this ISBN already exists. Not added to the library.
     ```
5. When the user chooses to **quit**:
   - Print out the contents of the library in a nice format, one book per line:
     ```
     Your Library:
     1. "Title" by Author (ISBN: 123...)
     ```

---

### **Example Run (Duplicate ISBN)**

```text
Do you want to add a book? (yes/no): yes
Enter the title: Dune
Enter the author: Frank Herbert
Enter the ISBN: 9780441172719

Do you want to add a book? (yes/no): yes
Enter the title: Another Dune
Enter the author: Someone Else
Enter the ISBN: 9780441172719
Book with this ISBN already exists. Not added to the library.

Do you want to add a book? (yes/no): no

Your Library:
1. "Dune" by Frank Herbert (ISBN: 9780441172719)
```

---

## **Step 2: Starter Code**

```python
# Name: Your Name
# CWID: Your CWID

def add_book(library, title, author, isbn):
    """
    Add a new book to the library if its ISBN is not already present.
    Return True if added, False if ISBN already exists.
    """
    # TODO: Write this function


def main():
    library = []  # start with an empty library

    while True:
        # TODO: prompt user ... This should be mostly the same
            

    print("\nYour Library:")
    

if __name__ == "__main__":
    main()
```

---

## **Why `if __name__ == "__main__": main()`?**

- **`__name__`** is a special Python variable.  
- When you **run a file directly** (e.g., `python3 library.py`), Python sets `__name__` to `"__main__"`.  
- When you **import** a file (e.g., your tests import `library.py`), `__name__` is set to the **module’s name**, **not** `"__main__"`.

**So:**
- Putting your program’s entry point under  
  ```python
  if __name__ == "__main__":
      main()
  ```  
  makes sure `main()` **only runs when the file is executed directly**, but **does not run** when it’s **imported** (e.g., by `check50` to test your functions).  
- If you just wrote `main()` at the bottom with no guard, then importing `library.py` in tests would **trigger your whole program** unintentionally.

---

## **How To Submit**
1. **Check your code** with check50  
   ```bash
   check50 citadelcs/problems/main/labs/lab04
   ```
2. **Submit your code** with submit50  
   ```bash
   submit50 citadelcs/problems/main/labs/lab04
   ```
3. **Upload your file** `library.py` to Canvas.  

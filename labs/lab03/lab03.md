# LAB03 — Simple Library Manager

## **Step 1: The Problem**

Create a new Python file called **`library.py`**.

At the **very top of your file**, include a comment with **your name and CWID** like this:

```python
# Name: John Doe
# CWID: 12345678
```

In this assignment you will model a **library** using Python data structures:

- A **book** will be a **dictionary** with at least two keys:
  - `"title"` → string  
  - `"author"` → string  
- The **library** will be a **list** of book dictionaries.

Your program should:

1. Start with an **empty library** (empty list).  
2. Write a function **`add_book(library, title, author)`** that creates a new book dictionary and appends it to the library.  
   - For now, this function should **not return anything**.  
   - *Next week*, you will extend it to check for duplicates and return `True`/`False`.  
3. Use a **loop** to repeatedly ask the user whether they want to **add a new book** or **quit**.  
4. When the user chooses to **add** a book:  
   - Prompt for the **title** and **author**.  
   - Call your **`add_book`** function.  
5. When the user chooses to **quit**:  
   - Print out the contents of the library in a nice format, one book per line.  

###### (NOTE: Copy the text provided in the examples given for correct checks is CS50)
---

### **Example Run 1**

```text
Do you want to add a book? (yes/no): yes
Enter the title: The Hobbit
Enter the author: J.R.R. Tolkien

Do you want to add a book? (yes/no): yes
Enter the title: Dune
Enter the author: Frank Herbert

Do you want to add a book? (yes/no): no

Your Library:
1. "The Hobbit" by J.R.R. Tolkien
2. "Dune" by Frank Herbert
```

### **Example Run 2 (Invalid Input)**

```text
Do you want to add a book? (yes/no): maybe
Please type 'yes' or 'no'.
Do you want to add a book? (yes/no): no

Your Library:
```
### **Example Run 3 (No Input)**
---
```text
Do you want to add a book? (yes/no): no

Your Library:
```
## **Step 2: Starter Code**

Copy this into your new file **`library.py`** and fill in the missing parts:

```python
# Name: Your Name
# CWID: Your CWID

def add_book(library, title, author) -> None:
    """
    Create a dictionary for the book and add it to the library list.
    For now, this function does not return anything.
    """
    
    return


def main():
    library = []  # start with an empty library

    
    # Print out the library
    print("\nYour Library:")
    
main()
```

---

## **Hints**

1. A **dictionary** stores key/value pairs:  
   ```python
   book = {"title": "Dune", "author": "Frank Herbert"}
   ```  
2. A **list** can hold many dictionaries:  
   ```python
   library = [book1, book2]
   ```  
3. Use **`.append()`** inside your **`add_book`** function to add a new book.  
4. Use a **for-loop with `range(len(library))`** to print each book with its number.  

---

## **How To Submit**

1. **Check your code** with check50  
   ```bash
   check50 citadelcs/problems/main/labs/lab03
   ```
2. **Submit your code** with submit50  
   ```bash
   submit50 citadelcs/problems/main/labs/lab03
   ```
3. **Upload your file** `library.py` to Canvas.  

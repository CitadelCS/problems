# LAB06

## **Calculator with Error Handling**

Create a new Python file called **`calculator.py`**

At the **very top of your file**, include a comment with **your name and CWID** like this:

```python
# Name: Your Name
# CWID: 12345678
```

---

### Program Requirements:

- Implement a **calculator** that repeatedly allows the user to:

  1. Select an operation by entering a number from the menu:

     ```
     1 - Add
     2 - Subtract
     3 - Multiply
     4 - Divide
     5 - Quit
     ```

  2. If the user enters `5`, the program should print:

     ```
     Goodbye!
     ```

     and then exit.

- For options 1-4:

  - Prompt the user to **enter two numbers** (accepts integers or floats).
  - Use a **function `get_number(prompt: str) -> float`** to get validated numeric input.
    - If the user inputs invalid numbers (like letters), print an error and prompt again.
  - Perform the selected operation.
    - If division by zero is attempted, print an error and prompt again for numbers.
  - Print the result in a user-friendly format.
  - Then show the menu again.

- **Use `try`/`except` blocks** to handle errors gracefully during number input and division.

- **Wrap your call to `main()` inside this block at the bottom of your file**:

```python
if __name__ == "__main__":
    main()
```

- Put **all print statements inside `main()` only**; your helper functions should not print anything.

---

### Suggested Function Signatures:

```python
def get_number(prompt: str) -> float:
    # TODO: Prompt for number, re-prompt on invalid input

def main():
    # TODO: Display menu, call get_number, perform operations, handle errors, etc.
```

---

### Example Runs:

#### Run 1:
```
1 - Add
2 - Subtract
3 - Multiply
4 - Divide
5 - Quit
Enter choice: 1
Enter first number: 10
Enter second number: 25.5
Result: 35.5

1 - Add
2 - Subtract
3 - Multiply
4 - Divide
5 - Quit
Enter choice: 5
Goodbye!
```

#### Run 2 (with errors):
```
1 - Add
2 - Subtract
3 - Multiply
4 - Divide
5 - Quit
Enter choice: 4
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero. Try again.
Enter first number: ten
Error: Please enter a valid number.
Enter first number: 10
Enter second number: 2
Result: 5.0
```

---

### How to Check Your Work:

```bash
check50 /citadelcs/problems/main/labs/lab05
```

---

### How to Submit:

**Step 1:**

```bash
submit50 /citadelcs/problems/main/labs/lab05
```

**Step 2:**

Upload your `calculator.py` file to Canvas.

---

### Reminder:

- Use `try`/`except` to handle invalid inputs and division errors.
- Do not call `main()` outside the `if __name__ == "__main__":` block.
- Keep all your `print()` statements in `main()` only.

---

Good luck and have fun coding! 🚀

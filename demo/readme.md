# CSCI 201 — Demo pset: Spot the Bug

Start by creating all six files (they can be empty for now):
```
touch problem1.py problem2.py problem3.py problem4.py problem5.py problem6.py
```

Run the autograder at any time with:
```
check50 CitadelCS/problems/main/demo
```

Work through each problem below, running `check50` after each fix to see your progress.

---

## Problem 1 — Type Error

Paste the following code into `problem1.py`:

```python
age = input("How old are you? ")
next_year = age + 1
print("Next year you'll be", next_year)
```

Run `check50`. You should see Problem 1 fail. Fix the bug so the program correctly calculates next year's age, then run `check50` again to confirm it passes.

---

## Problem 2 — Syntax Error

Paste the following code into `problem2.py`:

```python
score = 85
if score = 90:
    print("You got an A!")
else:
    print("Not an A.")
```

Run `check50`. You should see Problem 2 fail. Fix the bug so the program runs without error, then run `check50` again to confirm it passes.

---

## Problem 3 — Indentation Error

Paste the following code into `problem3.py`:

```python
for i in range(5):
    print(i)
        print("done")
```

Run `check50`. You should see Problem 3 fail. Fix the bug so the program runs without error, then run `check50` again to confirm it passes.

---

## Problem 4 — Off-by-One Error

Paste the following code into `problem4.py`:

```python
numbers = [10, 20, 30, 40, 50]
for i in range(1, len(numbers)):
    print(numbers[i])
```

Run `check50`. You should see Problem 4 fail. Fix the bug so all five numbers are printed, then run `check50` again to confirm it passes.

---

## Problem 5 — Name Error

Paste the following code into `problem5.py`:

```python
username = "Mike"
print("Welcome, " + usrname)
```

Run `check50`. You should see Problem 5 fail. Fix the bug so the program prints the correct welcome message, then run `check50` again to confirm it passes.

---

## Problem 6 — Write It Yourself

Create a file called `problem6.py`. Run `check50` — you'll see two failing checks. Read the check descriptions carefully: they tell you exactly what your program needs to print. Write the code to make both checks pass.

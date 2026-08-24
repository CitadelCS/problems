# CSCI 201 — Demo pset: Spot the Bug

Follow along with this practice pset to get used to editing files and using the autograder. You will use a similar workflow in future psets for a grade.
Before beginning, ensure you have completed the "Account Setup and Test Program" steps posted on Canvas.


Start by creating a folder for your work and navigating into it. First, log into [cs50.dev](https://cs50.dev), which will launch VSCode in the browser. Then, type the following commands in the terminal on the bottom.

```
mkdir demo
cd demo
```

Then create all six files (they can be empty for now):
```
touch problem1.py problem2.py problem3.py problem4.py problem5.py problem6.py
```

Run the autograder at any time with:
```
check50 CitadelCS/problems/main/demo
```

**Workflow tip:** Before running `check50`, always run your program locally first with `python problemN.py`. Reading the actual error message or output in your terminal is much faster for debugging than waiting on the autograder. Only use `check50` to confirm a fix is correct — not to discover what's wrong.

Work through each problem below using this loop: run locally → read the error → fix it → run locally again → confirm it works → run `check50`.

---

## Problem 1 — Type Error

Paste the following code into `problem1.py`:

```python
age = input("How old are you? ")
next_year = age + 1
print("Next year you'll be", next_year)
```

Run it locally:
```
python problem1.py
```

You'll see an error. Read the error message, fix the bug so the program correctly calculates next year's age, and run it locally again to confirm. Then run `check50` to verify.

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

Run it locally:
```
python problem2.py
```

You'll see an error. Fix the bug so the program runs without error, confirm locally, then run `check50`.

---

## Problem 3 — Indentation Error

Paste the following code into `problem3.py`:

```python
for i in range(5):
    print(i)
        print("done")
```

Run it locally:
```
python problem3.py
```

You'll see an error. Fix the bug so the program runs without error, confirm locally, then run `check50`.

---

## Problem 4 — Off-by-One Error

Paste the following code into `problem4.py`:

```python
numbers = [10, 20, 30, 40, 50]
for i in range(1, len(numbers)):
    print(numbers[i])
```

Run it locally:
```
python problem4.py
```

This one won't crash — but the output won't be right. Fix the bug so all five numbers are printed, confirm locally, then run `check50`.

---

## Problem 5 — Name Error

Paste the following code into `problem5.py`:

```python
username = "Mike"
print("Welcome, " + usrname)
```

Run it locally:
```
python problem5.py
```

You'll see an error. Fix the bug so the program prints the correct welcome message, confirm locally, then run `check50`.

---

## Problem 6 — Write It Yourself

Run `check50` — you'll see two failing checks for Problem 6. Read the check descriptions carefully: they tell you exactly what your program needs to print. Write the code in `problem6.py`, run it locally to confirm the output looks right, then run `check50` to verify.

---

## Submitting

Once all checks pass, submit your work with:
```
submit50 CitadelCS/problems/main/demo
```

**check50 vs. submit50:** `check50` runs the autograder and shows you the results — you can run it as many times as you want. It does not record anything. `submit50` does the same thing, but also uploads your files and records the submission. Run `check50` while you're working; run `submit50` when you're done.

**Important:** Your instructor cannot see your work from `check50` alone. You must run `submit50` for your submission to be received and graded.

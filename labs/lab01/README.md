# LAB01: Getting Started with Code

###### We will be installing VSCode to code locally in the event cs50.dev is down

---

## **Step 1: Download VSCode**

1. Download VSCode at [code.visualstudio.com/download](https://code.visualstudio.com/download)
2. Select the correct OS for your installation
3. Run the installer

## **Step 2: Connect it to your cs50.dev account**

1. Navigate to [cs50.dev](https://cs50.dev) 
2. **DO NOT CLICK `Log In`**
3. Click the Carrot (dropdown arrow)
4. Select `Open in VS Code Desktop`
   5. This will open VSCode and give you a popup
6. Click Install Extension and Open URI
7. Click Allow
8. Sign in to your GitHub account


## **Step 3: Coding**

Create a new python file called `simple_grader.py`

This program should take user input for the grade on an assignment.
For example: 

```text
Enter the Total Points of the assignment:    100
Enter the Points earned on the assignment:   85

Grade:  B
Score:  85.00%
```
The result should be the score of the assignment and a letter grade respectively


Starter Code:

```python3
def main():
   # Start Code here
   

def calc_score(points, total):
   # Code here
   
   return


main()
```

##### **Hints:**
1. To print the score rounded to 2 decimal places using f-string
`print(f"Rounded Score: {score:.2f}")`
2. You should account for a divide by zero error with the message `Error: Total points cannot be zero.`

## **How To Submit**
1. Check code with check50 <SLUG>
2. Submit code to cs50 with submit50 <SLUG>
3. Upload your `simple_grader.py` file to canvas

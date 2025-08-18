# problems
autograder checks for CSCI 201

https://cs50.readthedocs.io/projects/check50/en/latest/check_writer/#check-writer


`check50 --dev .` to create `__init__.py`. Run from `.cs50.yml` directory. Include ref soln in directory, then delete before push.

extra check for file exist

```python
@check50.check()
def exists():
    """indoor.py exists"""
    check50.exists("indoor.py")
```
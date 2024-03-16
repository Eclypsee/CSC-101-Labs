# Lab 7

## Instructions

Complete the following problem.

## Addition Program

In `lab07.py`, you will write a program that uses file handling to carry out arithmetic.

Your program must do the following:
- Read integers from `numbers.txt`, which contains lines with two integers each, separated by whitespace. Note that some lines may be improperly formatted.
- For each line with two valid integers, calculate their sum.
- Skip lines with invalid content without causing an error.
- Write (do not print) the results to a new file `output.txt` in the format `x + y = z`, one per line.

Implement error handling using `try` and `except` to manage lines that cannot be processed.
Convert strings to integers with the `int()` function.

### numbers.txt

```
1 2
3   4

    5   6
seven eight
9   10
11  twelve
thirteen 14
15
    16
17  18
```

### Several Expected output.txt Lines

```
1 + 2 = 3
3 + 4 = 7
5 + 6 = 11
...
```

(Note that the blank third line in `numbers.txt` should be ignored)

> [!IMPORTANT]
> 
> Your output file name must match `output.txt` exactly.
> Be sure to include a new line `'\n'` at the end of every written line.
> The last line in the file should exist, but be empty.

### File Handling Approaches
You can choose to open files either simultaneously or one after the other:

```python
# Simultaneous file handling
with open('numbers.txt') as r:
    with open('output.txt', 'w') as w:
        # The rest of your program
```

```python
# Sequential file handling
with open('numbers.txt') as r:
    lines = f.read()  # Read the lines to use when writing
with open('output.txt', 'w') as w:
    # Further processing and writing to output.txt
```
(Note the file variable names, recalling that they can be any valid name)

### The main() Function

Place all of your code within the included `main()` function.
This function is called under the main guard when you run the script.
Storing your program in a function like this allows for easy testing of your code.

```python
def main() -> None:
    # Write your file processing code here


if __name__ == '__main__':
    main()
```

## Validation

Before pushing to GitHub, you may run the `__autograde__.py` script to check your work.

> [!IMPORTANT]
> 
> **Do not** modify this file or your grade may be negatively impacted.

## Demonstration

To demonstrate this lab, you will show execution of your program to an instructor to verify its functionality.

## Submission

Commit and push your changes to GitHub. **You do not need to push your `output.txt` file.**

On Canvas, upload a screenshot showing proof of your submission from GitHub. **Your repository name must be visible.**

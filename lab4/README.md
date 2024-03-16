[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/kBrjq0Vb)
# Lab 4

## Course Information
- **Course:** CSC 101
- **Instructor:** Professor Vanessa Rivera
- **Term:** 2023-24 Winter Quarter

## Overview
In our previous lab and homework assignment, you practiced repetition using `while` loops.
In many programs, it is common to want some code to run repeatedly without duplicating the code or specifying a separate function call for each repetition.

In fact, there are times when we may not even know how many times the code should be repeated.
Consider processing the entries in your phone's collection of contacts; how many do you have? Is that the same for everybody?

This lab explores the evaluation of code utilizing two forms of repetition: list comprehensions and `for` loops.
These alternative to the `while` loop are specifically designed to iterate over a *collection* such as a list or string.

## Learning Objectives
In completing this assessment, you will be able to:
- Use PyCharm's debugger to analyze for loops and list comprehensions. (🧠, 🌐)

## Instructions
### Task 1: Tracing with Control Structures
**🎯 Task Goal:** Trace and answer questions about each program given below.

Independently trace and answer the questions for each program given below.

I **strongly** recommend you manually type in the code to build muscle memory so that the syntax becomes more familiar.

#### Program 1

```python
more = [x + 1 for x in [1,2,3,4]]  # Place a breakpoint on this line
print()
```

Write the above program in a unique file using PyCharm, run it with the debugger, and then write an answer to the following question(s) as part of your Canvas submission.

- **Question 1:** List, in order, the values that `x` takes at each step.
- **Question 2:** What is the value assigned to `more`?

#### Program 2

```python
def square(n: int) -> int:
    return n * n  # Place a breakpoint on this line

squares = [square(x) for x in [1, 2, 3, 4]]
print()
```

Write the above program in a unique file using PyCharm, run it with the debugger, and then write an answer to the following question(s) as part of your Canvas submission.

> [!TIP]
> 
> You can use the "Resume Program" button to have the PyCharm debugger run until it reaches the breakpoint again.

- **Question 1:** List, in order, the values that `n` takes each call and the value the function would return.
- **Question 2:** What is the value assigned to `squares` and how does it relate to the values determined in Question 1?

#### Program 3

```python
def check(n: int) -> bool:
    return n > 2  # Place a breakpoint on this line

answer = [x for x in range(5) if check(x)]
print()
```

Write the above program in a unique file using PyCharm, run it with the debugger, and then write an answer to the following question(s) as part of your Canvas submission.

- **Question 1:** List, in order, the values that `n` takes each call and the value the function would return.
- **Question 2:** What is the value assigned to `answer` and how does it relate to the values determined in Question 1?

#### Program 4

```python
def inc(m: int) -> int:
    return m + 1  # Place a breakpoint on this line

def check(n: int) -> bool:
    return n > 2  # Place a breakpoint on this line, too!


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer?
print()
```

Write the above program in a unique file using PyCharm, run it with the debugger, and then write an answer to the following question(s) as part of your Canvas submission.

- **Question 1:** List, in order, the values that `n` takes each call and the value the function would return.
- **Question 2:** List, in order, the values that `m` takes each call and the value the function would return.
- **Question 3:** What is the value assigned to `answer`?

## Task 2: Conditionals and Functions
**🎯 Task Goal:** Trace and answer questions about each program given below.

Independently trace and answer the questions for each program given below.

I **strongly** recommend you manually type in the code to build muscle memory so that the syntax becomes more familiar.

#### Program 1

```python
def tally(nums: list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num # Place a breakpoint here
    return total

result = tally([4, 9, 2, 1])
```

Write the above program in a unique file using PyCharm, run it with the debugger, and then write an answer to the following question(s) as part of your Canvas submission.

- **Question 1:** Record the value of `total` and `num` at the end of each iteration of the loop body.

#### Program 2

```python
def copy(nums: list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])
    return new_list

result = copy([4, 9, 2, 1])
```

Write the above program in a unique file using PyCharm, run it with the debugger, and then write an answer to the following question(s) as part of your Canvas submission.

- **Question 1:** Record the value of `new_list` and `idx` at the end of each iteration of the loop body.
- **Question 2:** How is this loop different from Program 1?

#### Program 3

```python
def increment_all(nums: list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)
    return new_list

result = increment_all([4, 9, 2, 1])
```

Write the above program in a unique file using PyCharm, run it with the debugger, and then write an answer to the following question(s) as part of your Canvas submission.

- **Question:** Record the value of `new_list` and `value` at the end of each iteration of the loop body.

## Task 3: Conditionals and Functions
**🎯 Task Goal:** Debug and fix the `summation` function in `summation.py`.

1. **Run the Tests:** Open `tests`.py` and run all the tests.
   You should see an indication that one failed (this is expected for the provided code).
   Read the failure message carefully.
   In particular, it is common to skip the "Traceback" portion because it is unpleasantly red and initially looks a bit cryptic.
   However, it tells us lots of helpful information such as the name of the file in which the test appears, then line on which the assertion failed, and the testing function that failed.
   We can also see the differences between the expected value and the actual value.
2. **Run the Debugger:** Place a breakpoint on the first line of `test_summation_2`, the testing method that failed, line 13, and then run the debugger.
3. **Step Through with the Debugger:** Repeatedly "Step Into" your code and examine the values assigned to `number` and added to `total`.
   Try to figure out what the program is doing wrong.
   If you are not sure what the issue is, discuss it with your peers or with your instructor.
4. **Correct the Issue:** After determining the issue, modify `summation.py` to fix it.
5. **Verification:** Run **all** the tests again to verify the issue is corrected.
6. **Submission:** Commit and push your code to GitHub, submitting a screenshot of your GitHub repository to Canvas as evidence of your submission.
   Answer the question below and submit it as part of your Canvas submission.

**Question:** If `test_summation_2` had been the only testing method, then all tests would have initially passed.
Would that have meant that the code was correct?
While waiting to demonstrate completion of the lab, ponder how many tests one might need to sufficiently test this function.

## Academic Integrity
> [!Warning]
> 
> Submitting this assignment confirms that you did not use solutions or code from external, AI-generated, or peer sources.
>
> You also agree to have your code checked by standard plagiarism detection software.
>
> Violation will result in a grade of zero, a report to the University, and further potential action.
>
> Please contact me or see our course syllabus for clarification or further details.

## Demonstration Success Guidelines
Demonstrate the following to complete this lab activity:
- **Task 1:** Show an instructor the recorded responses for each of the exercises.
- **Task 2:** Show an instructor the recorded responses for each of the exercises. 
- **Task 3:** Show an instructor the evaluation of the test cases and the corrected function.

## Success Checklist
- [ ] Traced programs and answered questions for Task 1. 
  - [ ] Program 1 is written in a unique file and answers to its questions are submitted to Canvas.
  - [ ] Program 2 is written in a unique file and answers to its questions are submitted to Canvas.
  - [ ] Program 3 is written in a unique file and answers to its questions are submitted to Canvas.
  - [ ] Program 4 is written in a unique file and answers to its questions are submitted to Canvas.
- [ ] Traced programs and answered questions for Task 2. 
  - [ ] Program 1 is written in a unique file and answers to its questions are submitted to Canvas.
  - [ ] Program 2 is written in a unique file and answers to its questions are submitted to Canvas.
  - [ ] Program 3 is written in a unique file and answers to its questions are submitted to Canvas.
- [ ] Fixed `summation.py` in Task 3.
  - [ ] All three tests pass.
  - [ ] Answered the question and submitted the answer to Canvas
- [ ] Completed the Canvas submission.
  - [ ] Ensured all new program files (Tasks 1 and 2) are committed and pushed to GitHub. 
  - [ ] Submitted a screenshot of your up-to-date GitHub repository to Canvas.
  - [ ] Submitted all work above.
- [ ] Completed the lab demonstration.
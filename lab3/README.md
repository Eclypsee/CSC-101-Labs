[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FJBYD4Fu)
# Lab 3

## Course Information
- **Course:** CSC 101
- **Instructor:** Professor Vanessa Rivera
- **Term:** 2023-24 Winter Quarter

## Overview
In this third lab, you will become familiar with control structures.
`if` and `while` statements allow us to redirect the otherwise linear "flow of execution" in our programs in interesting, and often complex ways.

First, you will analyze a program that uses conditionals and a while loop.
Next, you will fix some common errors that occur in the construction of chained conditionals.
Lastly, you will write a non-trivial function to calculate a sum of integers using a loop.

## Learning Objectives
In completing this assessment, you will be able to:
- Use PyCharm's debugger to analyze function calls containing control structures. (🧠, 🌐)
- Modify a function definition that uses conditionals. (💻)
- Write a function that utilizes a while loop. (💻)

## Instructions
### Task 1: Tracing with Control Structures
**🎯 Task Goal:** Trace the `conditionals.py`.

1. **Open the Script:** Open the `conditionals.py` script in the PyCharm editor and **place a breakpoint on line 15**.
2. **Complete Trace Tables:** Create trace tables for the script.
   You are recommended to use the PyCharm debugger with the "Step Into My Code" button.
   In addition to the main script itself, each call will require its own table.
   Templates for each table are provided below.
3. **New Data Type:** This program uses a *list* and the *`len`* function.
   You do not need to understand anything about lists or this function to complete this task.
   Simply write the values the debugger shows for each variable in your trace table.
4. **Submission:** Record your answers as part of your Canvas submission.

#### Table Templates

| Line |            the_cats             |       entire       |   partial    |
|-----:|:-------------------------------:|:------------------:|:------------:|
|   15 | `['mochi', 'harvest', 'pearl']` |                    |              |
|   17 |                -                | `'mochi harvest '` |              |
|   18 |                -                |         -          | `'harvest '` |
|   20 |                -                |         -          |      -       |

| Line |              cats               | i  |    concatenated    |
|-----:|:-------------------------------:|:--:|:------------------:|
|    4 | `['mochi', 'harvest', 'pearl']` | ?0 |                    |
|    5 |                -                | ?- |        `""`        |
|   10 |                -                | ?- |     `'mochi '`     |
|   11 |                -                | ?1 |         -          |
|   10 |                -                | ?- | `'mochi harvest '` |
|   11 |                -                | ?2 |         -          |
|    8 |                -                | ?3 |         -          |
|   12 |                -                | ?- |         -          |

| Line |              cats               | i  | concatenated |
|-----:|:-------------------------------:|:--:|:------------:|
|    4 | `['mochi', 'harvest', 'pearl']` | ?1 |              |
|    5 |                -                | ?- |     `""`     |
|   10 |                -                | ?- | `'harvest '` |
|   11 |                -                | ?2 |      -       |
|    8 |                -                | ?3 |      -       |
|   12 |                -                | ?- |      -       |

## Task 2: Conditionals and Functions
**🎯 Task Goal:** Modify the `roll` function in `dice.py` to meet the given requirements. 

**Background:** In the game *Dungeons and Dragons*, players roll a 20-sided die to determine whether their actions fail or succeed.
To emulate the game, the program in `dicepy` chooses a random number between 1 and 20 (inclusive) and then outputs a message based on the number chosen by calling the `roll` function.
The messages *should*, but do not, match the following criteria:
- **If a 1 is rolled:** "X Natural Miss"
- **If 2-10 (inclusive) is rolled:** "X Failure"
- **If 11-19 (inclusive) is rolled:** "X Success" 
- **If a 20 is rolled:** "X Critical Success!"

Where "X" is the value that was rolled.
As given **the program produces incorrect output** and sometimes produces **two** messages.

1. **Run the Script:** Open `dice.py` and execute the script multiple times to familiarize yourself with its behavior for different input values.
   You should see each scenario given above before moving to the next step.
2. **Modify the Script:** 
Modify the function by restructuring the `if`, `elif`, and `else` statements to produce a **single** message meeting the criteria above.
3. **Verification:** You may change the existing function call or write new ones within the main guard to test specific, instead of random, values.
4. **Submission:** Commit and push your `dice.py` changes to GitHub.

### Task 3: Write a Summation Function
**🎯 Task Goal:** Complete the function in `loop.py`.

1. **Write Two Unit Tests:** `summation.py` contains a template function definition for you to complete. 
   This function is intended to calculate the sum of integers (also known as triangular numbers) up to a given integer.
2. **Examples:** Given an integer `n`, the function should return the sum of all numbers from 0 up to `n`.
   For example, given a specific value of `n` the function would return the following values:
   - **`n = 1`:** `1`
   - **`n = 2`:** `1 + 2 = 3`
   - **`n = 3`:** `1 + 2 + 3 = 6`
   - **`n = 4`:** `1 + 2 + 3 + 4 = 10`
   - **`n = 5`:** `1 + 2 + 3 + 4 + 5 = 15`
   - etc.
3. **Hint:** Use the loop template given in the code and two variables: (1) a value representing an "iterator" for the current number (starting from 0 up to, and including `n`) and (2) a value representing the total, sum value.
   Be sure your loop condition can return `False` or your program may not terminate! 
4. **Submission:** Commit and push your `loop.py` changes to GitHub.
   Submit a screenshot to Canvas as evidence of your GitHub submission.

> [!Note]
> 
> It is possible (and much more efficient!) to write this function using a mathematical formula.
>
> You are encouraged to try writing a separate version that uses the formula for additional practice.

## Resources
- [wikipedia.org: Triangular Number](https://en.wikipedia.org/wiki/Triangular_number): Overview of triangular numbers.

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
This lab assigned during asynchronous class does not require a demonstration.

## Success Checklist
- [ ] Created a trace table for `conditionals.py`.
  - [ ] Created a trace table for the outer script.
  - [ ] Created a trace table for the first function call.
  - [ ] Created a trace table for the second function call.
- [ ] Modified the `roll` method in `dice.py`.
  - [ ] If a 1 is rolled, the program only prints "X Natural Miss"
  - [ ] If 2-10 (inclusive) is rolled, the program only prints "X Failure"
  - [ ] If 11-19 (inclusive) is rolled, the program only prints "X Success"
  - [ ] If a 20 is rolled, the program only prints "X Critical Success!"
  - [ ] Committed and pushed `dice.py` changes to GitHub.
- [ ] Completed the template definition in `summation.py`.
  - [ ] The function meets the listed return value requirements.
  - [ ] Committed and pushed `summation.py` changes to GitHub.
- [ ] Completed the Canvas submission.
  - [ ] Submitted a screenshot of your up-to-date GitHub repository to Canvas.
  - [ ] Submitted your trace table to Canvas. 
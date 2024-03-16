[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y10lslSL)
# Lab 2

## Course Information
- **Course:** CSC 101
- **Instructor:** Professor Vanessa Rivera
- **Term:** 2023-24 Winter Quarter

## Overview
In this second lab, you will become familiar with functions by working with them in a variety of ways.
Functions are essential units used to build large, complex computer programs.

First, you will analyze a program that interacts with the call stack.
Next, you will write your own function definition.
Lastly, you will write unit tests to verify your function.

## Learning Objectives
In completing this assessment, you will be able to:
- Use PyCharm's debugger to analyze function calls. (🧠, 🌐)
- Write a simple parameterized function that returns a value. (💻)
- Include a docstring and type annotations for a function definition. (✍️)
- Write unit tests for a simple function definition. (🧪)

## Instructions
### Task 1: Tracing with Function Calls
**🎯 Task Goal:** Trace the `calls.py` script.

1. **Open the Script:** Open the `calls.py` script in the PyCharm editor and **place a breakpoint on line 20**.
2. **Complete Trace Tables:** Create trace tables for the script.
   You are recommended to use the PyCharm debugger with the "Step Into My Code" button.
   In addition to the main script itself, each call will require its own table.
   Templates for each table are provided below.
3. **Submission:** Record your answers as part of your Canvas submission.

#### Table Templates
| Line | result |
|-----:|:------:|
|   20 |  0.5   |
|   21 |   -    |

| line | x   | y   | magnitude |
|------|-----|-----|-----------|
| 13   | -   | -   | -         |
| 15   | 3.0 | 4.0 | 5.0       |
| 16   | -   | -   | -         |


| line | x_1 | y_1 | x_2 | y_2 | dx  | dy  |
|------|-----|-----|-----|-----|-----|-----|
| 6    | -   | -   | -   | -   | -   | -   |
| 8    | 0   | 0   | 3.0 | 4.0 | 3.0 | -   |
| 9    |     |     |     |     |     | 4.0 |
| 10   | -   | -   | -   | -   | -   | -   |




### Task 2: Write a Function Definition
**🎯 Task Goal:** Write the `get_max_quarters` function.

1. **Define the Function:** In `coins.py`, define a function called `get_max_quarters`.
2. **Requirements:** This function should meet the following requirements:
   - **Input:** This function should accept a parameter of type `int`, representing the number of cents.
   - **Output:** This function should return a value of type `int`, representing the maximum number of quarters that can be obtained from the given cents.
   - **Example:** The function call `get_max_quarters(360)` would evaluate to `14`.
   - **Documentation:** The function should contain a docstring and type annotations.
   - **Verification:** You may verify the behavior of your function using `print` statements within a main guard.
3. **Submission:** Commit and push your `coins.py` changes to GitHub.
   You will submit a screenshot to Canvas as evidence of your GitHub submission. 

### Task 3: Write Unit Tests
**🎯 Task Goal:** Write two unit test functions for `get_max_quarters`.

1. **Write Two Unit Tests:** In `coins_tests.py`, add two new, unique, unit test functions within the `CoinsTest` class.
   This script imports `get_max_quarters` for you and contains an example unit test function.
2. **Requirements:** Each test should contain three components:
   - **Arguments:** You should determine an argument to pass to `get_max_quarters` for each test. 
   - **Expected Value:** For each test, determine an expected value based on your argument.
   - **Actual Value:** Within each test, you should perform a function call to `get_max_quarters`, passing in the appropriate argument.
   - **Assertion Statement:** Perform the actual test using the appropriate assertion statement.
3. **Verification:** You may run your tests by running `coins_tests.py`.
   You should see a message that three tests have passed (this includes the given example).
4. **Submission:** Commit and push your `coins_tests.py` changes to GitHub.
   Submit a screenshot to Canvas as evidence of your GitHub submission.

## Resources
- [docs.python.org: unittest - Unit Testing Framework](https://docs.python.org/3/library/unittest.html): Documentation for the `unittest` library.

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
Be able to:
* Show your Task 1 trace tables.
* Demonstrate usage of the "Step Into My Code" button.
* Show and explain your function definition.
* Explain how to write a unit test for your function.
* Show your GitHub.com repository containing your pushed code.
* Show your Canvas submission.

*Note: Your critical-thinking skills and ability to articulate your understanding will be assessed. You should be able to answer questions in your own words, without merely reading lines of code or comments.*

## Success Checklist
- [ ] Created a trace table for `calls.py`.
  - [ ] Created a trace table for the outer script.
  - [ ] Created a trace table for the first function call.
  - [ ] Created a trace table for the second function call.
- [ ] Completed the definition for `get_max_quarters`.
  - [ ] The function performs the intended behavior.
  - [ ] The definition contains type annotations.
  - [ ] The definition contains a docstring.
- [ ] Completed two unit tests for `get_max_quarters`.
  - [ ] Wrote a first, unique, unit test method in `coins_tests.py`
    - [ ] The function is correctly located under the included class.
    - [ ] The function's name begins with "test".
    - [ ] The function calculates an actual value.
    - [ ] The function contains a passing assertion statement using an expected and actual value.
  - [ ] Wrote a second, unique, unit test method in `coins_tests.py`
    - [ ] The function is correctly located under the included class.
    - [ ] The function's name begins with "test".
    - [ ] The function calculates an actual value.
    - [ ] The function contains a passing assertion statement using an expected and actual value.
- [ ] Demonstrated your lab to an instructor.
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/jxptyf4t)
## Overview

Sorting is a common everyday operation.
Text messages are sorted *chronologically*.
Contacts in your phone are likely sorted by *priority*.
Because they are so fundamental, many programming languages have built-in sorting functions.

In the context of this course, sorting operations act as a next step in algorithmic complexity after map and filter patterns.
In this lab, you will modify an existing sorting method (selection sort) to manipulate lists of data in specific ways.

## Course Learning Objectives
### Direct

- 💻 Describe the basic syntax and semantics of a modern programming language, including variables, data types, expressions, and statements.
- ✍️ Assess the quality of Python code with respect to readability, maintainability, and adherence to standard conventions.
- 🧪 Design and implement a set of unit tests to validate program functionality, including edge cases.

### Indirect

- 🌐 Utilize a modern, networked development environment, including usage of an industry standard IDE and version control platforms.
- 🧠 Analyze the execution of a nontrivial computer program using a mental model of computation.

## Instructions

The included code contains a selection sort implementation along with several tests.
As is, the function operates on integer values.
Selection sort is independent of data type, provided appropriate comparisons are used.
You will create a new version of this function that operates on non-integer values.

For each of the following three (3) tasks, you are expected to add (at least) one function to the `function_definitions.py` file and at least two (2) test cases to the `function_tests.py` file.

You are expected to follow the *design recipe* outlined below for each function definition:

- Briefly state the purpose of the function, including its input and output. 
- Identify the representation of the data to be used in the computation. 
- Name and template the function.
- Do computation **by hand** and write tests.
- Complete the function implementation.

Your functions must follow the style guidelines outlined in the rubric for full credit.

### Task 1

Define a function named `selection_sort_books`.
The function must take a single parameter of type `list[Book]`.
This function will sort the provided list of books by *title* in alphabetical order.
Repurpose the provided selection sort function to do so.

Your solution must include *at least* two unit tests (an empty list is a reasonable test here).

### Task 2

Define a function named `swap_case`.
The function must accept a single parameter of type `str`.
The function must return a string identical to the input string, except that all lowercase letters must be converted to uppercase and visa-versa.

You are suggested to use the following string methods: `str.isalpha`, `str.islower`, `str.isupper`, `str.lower`, and `str.upper` functions.

Your solution must include *at least* two unit tests. You should consider testing with strings that include non-English letters.

#### Example Call(s)
```python
print(swap_case('aBcDeF!'))  # Output: AbCdEf!
print(swap_case('ááááÁÁÁÁ'))  # Output: ÁÁÁÁáááá
```

### Task 3

Define a function named `str_translate`.
The function must accept 3 parameters: (1) a string to modify, (2) a character to be replaced in the original string, (3) the character to replace with.
The function must return the original string except all instances of the first input character are replaced with the second input character.

**You are required to write this function without using any predefined string functions with similar behavior.**
Treat this as an exercise in implementing a library function.

Your solution must include *at least* two unit tests.

#### Example Call(s)
```python
print(str_translate('abcdcba', 'a', 'x'))  # Output: 'xbcdcbx'
```

## Demonstration
To complete this lab, show an instructor your function definitions, test cases, and a run of your (passing) tests.

**You will be graded at the time of demonstration** based on the functionality of your code, your unit tests, and style guideline adherence.

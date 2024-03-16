## Overview

In this lab, you will transition from debugging problems to solely focusing on writing functions.

These functions will utilize lists and classes in some form, as will all functions you write in the remainder of this course.

## Course Learning Objects

### Direct
- ✍️ Assess the quality of Python code in terms of readability, maintainability, and adherence to standard conventions.
- 🧪 Design and implement a set of unit tests to validate program functionality, including edge cases.

### Indirect
- 💻 Describe the basic syntax and semantics of a modern programming language, including variables, data types, expressions, and statements.
- 🌐 Utilize a modern, networked development environment including usage of industry-standard IDE and version control platforms.
- 🧠 Analyze the execution of a non-trivial computer program using a mental model of computation.

## Instructions

For each of the following six (6) tasks, you are expected to add (at least) one function to the `function_definitions.py` file and at least two (2) test cases to the `function_tests.py` file.

You are expected to follow the *design recipe* outlined below for each function definition:
- Briefly state the purpose of the function including its input and output. 
- Identify the representation of the data to be used in the computation. 
- Name and template the function.
- Do computation **by hand** and write tests.
- Complete the function implementation.

Your functions must follow the style guidelines outlined in the rubric for full credit.

### Task 1
Define a function named `first_element`.
The function must take one parameter of type `list[list[float]]` (that is, a list of nested floating-point containing lists).
The function must return a list containing the first element of each nested list.
If a nested list contains no elements itself, that nested list will be ignored.
The output list should be ordered corresponding to the input list.

### Task 2
Define a function named `x_coordinates`.
The function must take one parameter of type `list[Point]`.
The function must return a list containing the x-coordinate of each point.
The output list should be ordered corresponding to the input list.

> [!TIP]
>
> You may infer this function's output type by examining the `Point` class.

### Task 3
Define a function named `are_in_positive_quadrant`.
The function must take one parameter of type `list[Point]`.
The function must return all points from the input list that are in the first quadrant (i.e., their x and y values are *strictly* positive).
The output list should be ordered corresponding to the input list.

### Task 4
Define a function named `distance`.
The function must accept two parameters of type `Point`.
The function must return the [Euclidean Distance](https://en.wikipedia.org/wiki/Euclidean_distance) between the two points.

### Task 5
Define a function named `manhattan_distance`.
The function must accept two parameters of type `Point`.
The function must return the [Manhattan Distance](https://en.wikipedia.org/wiki/Manhattan_distance) between the two points.

### Task 6
Define a function named `origin_distances`.
The function must accept two parameters of type `Point`.
The function must return a list of distances from the origin corresponding to each point.
The output list should be ordered corresponding to the input list.

Use a distance function of your choice (see, Task 4 or Task 5) in your implementation of this function.

## Demonstration
To complete this lab, show an instructor your function definitions, test cases, and a run of your (passing) tests.

**You will be graded at the time of demonstration** based on the functionality of your code, your unit tests, and style guideline adherence.

# Homework 6

## Course Information

- **Course Name:** CSC 101
- **Instructor:** Vanessa Rivera
- **Term:** 2023-24 Winter Quarter

## Overview

This assignment is an extension of the `Creature` class and functionality you implemented in Homework 5.
Here, you will write a program that reads custom **script** files to interact with a database (list) of `Creature` objects.
In professional programming environments, automating tasks through scripts and efficiently managing data are common practices.
This assignment is designed to give you a taste of such real-world scenarios.
For example, your program might be used to quickly assess the statistics of the `Creatures` to inform game balance design decisions.

## Learning Objectives

In completing this assessment, you will be able to:

- Write a complex program that produces non-trivial input/output functions.
- Synthesize a program from multiple distinct parts: a class, file handling, lists, and functions.
- Utilize command-line arguments to change the functionality of a program.

## Instructions

### Task 1: Copy Homework 5 Files

- **Description:** Copy and paste your completed Homework 5 `Creature` class into Homework 6's `creature.py`.
  It is highly recommended, but not strictly required, to copy your Homework 5 functions into Homework 6's `functions.py`.
  A completed `Creature` class is required for the program you will be writing.
- **Requirements:**
  - The `Creature` class must be fully implemented.
  - (Optional) Your Homework 6 functions may be copied and pasted into `functions.py`.
    - Do not erase the `list_to_creature()`, `report_creature()`, or `load_creatures_text_file()` functions included in Homework 6.

### Task 2: Write the Creature File Reading Function

- **Description:** Write a function called `load_creatures_text_file(file_path: str) -> list[Creature]`.
  This function will accept a path to a file as a single string and output a list of `Creature` objects.
  his function is intended to read files of the same format as the included `creatures.txt` file.
  Each non-blank line in this file contains information to create a single `Creature` object.
  Your function should create an empty list, open the specified file for writing, iterate on each line, and pass a relevant list of strings (use the `split()` method) to the included `list_to_creature()` function to produce a `Creature` object, and finally return a list of all such objects.
- **Requirements:**
  - Your function should produce a single `Creature` object for each non-blank line in the input file.
  - Your function must return a list of `Creature` objects.
  - Your function must ignore blank lines in a file.
  - You may, but are not required, to handle situations where the file doesn't exist.

### Task 3: Complete the Script Reading Program

- **Description:** Finish `program.py`.
  This program will treat a list as a database of creatures.
  Your program will read script files, like those within the `scripts` directory, and perform a series of operations on the database list.
  Comments within the file provide a guide and starting point.
- **Requirements:**
  - Your program must obtain a file path from the user, as given in the file 
  - Your program must read through all lines in the specified script file, ignoring any blank lines.
  - Your program must perform each operation specified in the script file.
    - Each operation is described below in the "Additional Notes" section.
  - Operations that change the database list should be cumulative, do not reload the list for each operation.
  - Your program should load the database using the `cscreatures.txt` file.
  - Your program should produce the expected output for each included script file.

### Bonus Points

An additional 50% of your score on this project will be applied to "Homework" grade category.
Your "Homework" category score may not exceed 80 points.

## Submission Guidelines

- **Due Date:** March 20 at 7:00 PM
- **Submission Format(s):**
  - **GitHub:** Commit and push your code to GitHub.
  - **Canvas:** A screenshot showing your GitHub.com repository of evidence of your commit and push.
- **Late Submission Policy:** Late submissions will **not** be accepted for this final homework.

## Academic Integrity

> [!Warning]
>
> Submitting this assignment confirms that you did not use solutions or code from external, AI-generated, or peer sources.
>
> You also agree to have your code checked by standard plagiarism detection software.
>
> Violation will result in a grade of zero, a report to the University, and further potential action.

## Additional Notes

### Operations

Your program will accept a file path to a script file from the user and then iterate through the lines in the file.
Non-blank lines in this file each contain an "operation" for your program to carry out.
These operations have specific behaviors that typically involve calling a function.

Some operations utilize and are followed by parameters.
The values of parameters are separated by colons (":") and the types are indicated by either "INT" (for integer) or "STR" (for string).
You will need to process each line of text to extract these parameters, converting the text into the appropriate type if necessary.
Be sure to appropriately handle or remove any unneeded whitespace as you read the script text file.
**You may do so using the `split()` and `strip()` string methods.**

As an example, the following line of text could represent an operation in one of the script files:

```
filter-by-attr-gt:resilience:30
```

This line is referring to the `filter-by-attr-gt` operation.
It has two parameters `resilience` which is a string and `30` which is an integer.
As described below, when your program carries out this function, it will reassign the database list to the same list except all creatures with a `resilience` attribute of 30 or less are removed.

The behavior of the specific operations you must handle in your program are as follows:
- `load`: This operation will reassign the database list to a new list containing all creatures from the `cscreatures.txt` text file. 
  You must use the  `load_creatures_text_file` function defined in week one.
  This operation will print the text:
  
  ```Loaded X entries```
  
  Where "X" is the size of the resulting list.
- `report-creatures`: This operation will iterate through each creature in the database list and pass it the `report_creature` function.
- `report-count`: This operation will print the following text:
  
  ```X entries```
  
  Where "X" is the size (`len()`) of the database list.
- `report-avg-exp`: This operation will print the following text:
  
  ```Experience Average: X```
  
  Where "X" is the sum total of each creature's attributes (resilience, courage, willpower, and determination) in the database list divided by the number of creatures.
  If the database list is empty, "X" should be a (floating-point) zero.
  You are recommended to use your `get_total_experience()` function from Homework 5.
- `report-avg-attr:STR`: This operation will print the following text:
  
  ```STR Average: X```
  
  Where "STR" is the given string that represents a `Creature` object’s attribute ("resilience", etc.) and "X" is the average value of that attribute among **all** creatures in the database list.
  If the given "STR" is not an attribute of the `Creature` class, "X" will be a (floating point) zero.
  You are recommended to use the `get_attribute()` function from Homework 5. 
- `report-percent-by-kind:STR`: This operation will print the following text:
  
  ```X% STR```
  
  Where "X" is the percent of creatures in the database list that have the given string in their list of `kinds` and "STR" is the given string.
  You are recommended to use the `has_kind()` function from Homework 5.
- `filter-by-kind:STR`: This operation will reassign the database list to a new list containing only `Creature` objects from the current database list that have the given string in their list of `kinds`.
  This operation will also print the following text:
  
  ```Filtered to X entries```

  Where "X" is the size of the resulting list.
  You are recommended to use the `filter_by_kind()` function from Homework 5.
- `filter-by-attr-lt:STR:INT`: This operation will reassign the database list to a new list containing only `Creature` objects from the current database list with an attribute value corresponding to the given by the string "STR" strictly less than the integer given by "INT".
  This operation will also print the following text:
  
  ```Filtered to X entries```
  
  Where "X" is the size of the resulting list.
  If the given "STR" is not an attribute of the `Creature` class, assume the attribute value is 0 for comparing to "INT".
  You are recommended to use the `filter_by_attribute_less_than()` function from Homework 5.
- `filter-by-attr-gt:STR:INT`: This operation will reassign the database list to a new list containing only `Creature` objects from the current database list with an attribute value corresponding to the given by the string "STR" strictly greater than the integer given by "INT".
  This operation will also print the following text:
  
  ```Filtered to X entries```
  
  Where "X" is the size of the resulting list.
  If the given "STR" is not an attribute of the `Creature` class, assume the attribute value is 0 for comparing to "INT".
  You are recommended to use the `filter_by_attribute_greater_than()` function from Homework 5.

### Included Scripts and Outputs

Included in the project directory is a `scripts` folder containing several scripts your program should be capable of running.
Each script contains a series of operations to perform using the creature database.
Your program will ask for the file path to one of these scripts to read upon execution.

Below are the content of each script and the expected output when read by your program:
- `scripts/cowardlyfire`
  - **File Contents:**
    
    ```
    load
    filter-by-attr-lt:courage:24
    filter-by-kind:fire
    report-creatures
    ```
  - **Expected Program Output:**
    
    ```
    Loaded 152 entries
    Filtered to 11 entries
    Filtered to 0 entries
    ```
- `scripts/determinedandwillful`
  - **File Contents:**
    
    ```
    load
    filter-by-attr-gt:determination:240
    filter-by-attr-gt:willpower:240
    report-creatures
    ```
  - **Expected Program Output:**
    
    ```
    Loaded 152 entries
    Filtered to 20 entries
    Filtered to 1 entries
    Smlogue
            IDNO: 114
            KIND: ['toxic', 'wind']
            HGHT: 002.8
            WGHT: 001.0
            FRND: 052
            RESI: 016
            COUR: 255
            WILL: 249
            LGND: False
            DESC: This is a creature to be feared. It can create a dense, poisonous fog that engulfs and incapacitates its enemies.
    ```
- `scripts/generalstatistics`
  - **File Contents:**
    
    ```
    load
    report-avg-exp
    report-avg-attr:resilience
    report-avg-attr:courage
    report-avg-attr:willpower
    report-avg-attr:determination
    report-percent-by-kind:nature
    report-percent-by-kind:fire
    report-percent-by-kind:water
    report-percent-by-kind:light
    report-percent-by-kind:dark
    report-percent-by-kind:electric
    report-percent-by-kind:ice
    report-percent-by-kind:earth
    report-percent-by-kind:metal
    report-percent-by-kind:wind
    report-percent-by-kind:toxic
    ```
  - **Expected Program Output:**
    
    ```
    Loaded 152 entries
    Experience Average: 573.5
    resilience Average: 139.1
    courage Average: 128.4
    willpower Average: 161.2
    determination Average: 144.7
    20.4% nature
    11.8% fire
    15.1% water
    16.4% light
    11.8% dark
    10.5% electric
    12.5% ice
    15.1% earth
    14.5% metal
    15.1% wind
    9.9% toxic
    ```
- `scripts/resilientwater`
  - **File Contents:**
    
    ```
    load
    filter-by-kind:water
    filter-by-attr-gt:resilience:220
    report-creatures
    ```
  - **Expected Program Output:**
    
    ```
    Loaded 152 entries
    Filtered to 23 entries
    Filtered to 3 entries
    Hydravine
            IDNO: 069
            KIND: ['nature', 'water']
            HGHT: 002.5
            WGHT: 097.0
            FRND: 081
            RESI: 224
            COUR: 214
            WILL: 226
            LGND: False
            DESC: A massive serpent covered in leaves that glisten with water. It lives for centuries as it requires no external nutrients.
    Mountshell
            IDNO: 126
            KIND: ['earth', 'water']
            HGHT: 003.0
            WGHT: 793.0
            FRND: 091
            RESI: 241
            COUR: 118
            WILL: 240
            LGND: False
            DESC: "Its massive shell resembles a mountain and even has a ravine."
    Neptunea
            IDNO: 145
            KIND: ['water', 'nature']
            HGHT: 001.7
            WGHT: 065.3
            FRND: 153
            RESI: 225
            COUR: 189
            WILL: 255
            LGND: True
            DESC: Neptunea is a serene aquatic creature. Its melodies are said to resonate with the deep sea, and it has the ability to predict upcoming events. 
    ```
- `scripts/testloading`
  - **File Contents:**
    
    ```
    report-count
    load
    report-count
    ```
  - **Expected Program Output:**
    
    ```
    0 entries
    Loaded 152 entries
    152 entries
    ```
   
## Success Checklist
- [ ] The `Creature` class is complete with `__init__`, `__str__` and `__eq__` methods.
- [ ] The `load_creatures_text_file()` function is implemented and creates a list of `Creature` objects based on a file.
  - [ ] The function ignores blank lines in the input file.
  - [ ] The function produces a list of 152 elements when using the included data file.
- [ ] The program handles and performs each operation.
  - [ ] The program handles the `load` operation.
  - [ ] The program handles the `report-creatures` operation.
  - [ ] The program handles the `report-count` operation.
  - [ ] The program handles the `report-avg-exp` operation.
  - [ ] The program handles the `report-avg-attr` operation and its string parameter.
  - [ ] The program handles the `report-percent-by-kind` operation and its string parameter.
  - [ ] The program handles the `filter-by-attr-lt` operation and its string and integer parameters.
  - [ ] The program handles the `filter-by-attr-gt` operation and its string and parameters.
- [ ] The program produces the expected output for each included script.
  - [ ] The program produces the expected output for the `scripts\cowardlyfire` script.
  - [ ] The program produces the expected output for the `scripts\determinedandwillful` script.
  - [ ] The program produces the expected output for the `scripts\generalstatistics` script.
  - [ ] The program produces the expected output for the `scripts\resilientwater` script.
  - [ ] The program produces the expected output for the `scripts\testloading` script.
- [ ] Your work is committed and pushed to GitHub.
- [ ] You've included a screenshot of your GitHub repository in your Canvas Submission.
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/WczsAYup)
# Homework 5

## Overview

In this assignment, you'll gain hands-on experience working with a large, complex database (a list of objects) in the context of developing a hypothetical game called "CS Creatures".
This game features 150 (or more to see) unique creatures, each with a variety of attributes, to befriend, train, and battle.

The game design team could benefit from tools to analyze the creature database.
This analysis would help understand how changes to individual creature designs might affect the overall game statistics and balance.

Your task is to develop a Python class to hold data on creatures and write functions that interact with objects of this class.

## Learning Objectives

### Direct

- 🌐 Utilize a modern, networked development environment including usage of industry-standard IDE and version control platforms.
- 🧪 Design and implement a set of unit tests to validate program functionality, including edge cases.

### Indirect

- 💻 Describe the basic syntax and semantics of a modern programming language, including variables, data types, expressions, and statements.
- ✍️ Assess the quality of Python code in terms of readability, maintainability, and adherence to standard conventions.
- 🧠 Analyze the execution of a non-trivial computer program using a mental model of computation.

## Instructions

## Task 1: The Creature Class and Tests

In `creature.py`, complete the `Creature` class.
This class should consist of the following:
- A docstring that briefly describes the class's purpose.
  - An `__init__` method, that accepts the following parameters to initialize corresponding attributes:
    1. `number: int`
    2. `name: str`
    3. `kinds: list[str]`
    4. `height: float`
    5. `weight: float`
    6. `friendliness: int`
    7. `resilience: int`
    8. `courage: int`
    9. `willpower: int`
    10. `determination: int`
    11. `legendary: bool`
    12. `description: str`
  
    Ensure you use type annotations for clarity.
- A `__str__` method with complete parameter and return type annotations that outputs a string of the following form:
  - **Example Call:** `str(Creature(0, 'a', ['b'], 1., 2., 1, 2, 3, 4, 5, False, 'c'))`
  - **Example Return:** `"Creature(number=0, name='a', kinds=['b'], height=1.0, weight=2.0, friendliness=1, resilience=2, courage=3, willpower=4, determination=5, legendary=False, description='c')"`
  - **Tips:** Be sure to include single quotation marks around string values, use proper spacing, and do not add any line breaks to the string.
- An `__eq__` method that should return `True` if a `Creature` object is being compared to another `Creature` object with equivalent attribute values.

You may run the included `creature_tests` file to ensure your implementation is correct.

> [!NOTE]
> 
> You can split a long expression into multiple lines by enclosing it within a single set of parentheses `()`.

## Task 2: Design Pattern Functions and Testing

### The Creature Database

With the `Creature` class complete, you now have access to the entire creature dataset in the form of a `list[Creature]`.

Two such lists are imported within `functions.py` and `function_tests.py` for you to use: (1) the entire database of 152 creatures called `CREATURES` and (2) a small subset of 10 creatures called `CREATURES_BLUE`.
A third list called `CREATURES_RED` is also included for the example function calls and test cases.

The following tables list the contents for selected attributes of the `CREATURES_RED` and `CREATURES_BLUE` lists for reference.
Because the `CREATURES` list is very large (152 elements), it is not displayed here.

You can display the information of all three lists, including all the unused attributes, by running the `print_creatures.py` file.

#### CREATURES_RED

| Name         |    Kinds     | Resilience | Courage | Willpower | Determination | Description                                                                                                                                                                                                                                                                                           |
|:-------------|:------------:|:----------:|:-------:|:---------:|:-------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dinospore    |    nature    |    117     |   79    |    100    |      69       | A small dinosaur that has a symbiotic relationship with a plant.                                                                                                                                                                                                                                      |
| Emberspark   |     fire     |     77     |   147   |    41     |      87       | A tiny salamander-like creature with a tail that's constantly ablaze. It is very playful and loves to chase its own fire sparks.                                                                                                                                                                      |
| Ripplefin    |    water     |     84     |   72    |    131    |      33       | A small fish-like creature that enjoys jumping out of the water to make a big splash. It uses its tail to move quickly in the water.                                                                                                                                                                  |
| Slumberbug   | dark, nature |    173     |   125   |    89     |      182      | A small, nocturnal insect with sleep-inducing powers. It can release a cloud of pollen to put enemies to sleep.                                                                                                                                                                                       |
| Shadowgnome  |  dark, fire  |     86     |   132   |    120    |      212      | A gnome-like creature that manipulates shadow-like bursts of energy. It's less friendly, preferring to lurk in the shadows and avoid interaction.                                                                                                                                                     |
| Emberfox     |     fire     |    136     |   137   |    142    |      118      | A fox-like creature with a tail that burns like a flame. It's friendly but can be a bit mischievous.                                                                                                                                                                                                  |
| Nightgale    |  dark, wind  |    135     |   120   |    251    |      217      | This calm bird is a creature of the night. Its dark feathers shimmer under the moonlight and its silent flight is a sight to behold.                                                                                                                                                                  |
| Urania       | wind, earth  |    164     |   215   |    170    |      255      | Urania is a dynamic creature that controls the winds. Its strong, earthy constitution makes it a formidable opponent.                                                                                                                                                                                 |
| Harvinger    |  fire, dark  |    176     |   198   |    67     |      218      | Harvinger is a legendary cat believed to control the underworld with a fiery spirit and an aggressive demeanor. It can unleash devastating fire attacks while shrouding itself in darkness to strike fear into its enemies. Harvinger is notorious for its relentless hunger and unyielding ferocity. |
| Pearlificent |    light     |    192     |   192   |    192    |      192      | Not much is known about this creature. Its existence is constantly refuted.                                                                                                                                                                                                                           |

#### CREATURES_BLUE

| Name          |     Kinds     | Resilience | Courage | Willpower | Determination | Description                                                                                                                                                                                                                                                              |
|:--------------|:-------------:|:----------:|:-------:|:---------:|:-------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dinospore     |    nature     |    117     |   79    |    100    |      69       | A small dinosaur that has a symbiotic relationship with a plant.                                                                                                                                                                                                         |
| Emberspark    |     fire      |     77     |   147   |    41     |      87       | A tiny salamander-like creature with a tail that's constantly ablaze. It is very playful and loves to chase its own fire sparks.                                                                                                                                         |
| Ripplefin     |     water     |     84     |   72    |    131    |      33       | A small fish-like creature that enjoys jumping out of the water to make a big splash. It uses its tail to move quickly in the water.                                                                                                                                     |
| Lumiworm      | light, nature |    127     |   104   |    140    |      75       | A tiny, glowing worm-like creature that emits a warm, comforting light. It can use its bioluminescence to communicate with others of its kind.                                                                                                                           |
| Lanternsprite |  light, fire  |    133     |   217   |    80     |      115      | A sprite-like creature that carries a lantern of enchanted fire. It is friendly and its warm light can guide travellers safely through the darkest nights.                                                                                                               |
| Frostkit      |      ice      |     16     |   129   |    88     |      248      | A small creature that resembles a snowy fox kit. It thrives in cold environments and can freeze the moisture in the air to create small snowstorms.                                                                                                                      |
| Voltantler    | electric, ice |     0      |   225   |    25     |      255      | Its antlers are like lightning rods and its body is covered with frosty fur that sparkles under the moonlight. It guides wanderers amid snowstorms.                                                                                                                      |
| Neptunea      | water, nature |    225     |   189   |    255    |      172      | Neptunea is a serene aquatic creature. Its melodies are said to resonate with the deep sea, and it has the ability to predict upcoming events.                                                                                                                           |
| Moracle       |  ice, light   |     63     |   214   |    188    |      222      | Moracle is an elegant, legendary cat believed to control the heavens. Its graceful movements are accompanied by a trail of frost, and it can emit blinding light to disorient those with dark intentions. Moracle is known for its serene demeanor and formidable power. |
| Pearlificent  |     light     |    192     |   192   |    192    |      192      | Not much is known about this creature. Its existence is constantly refuted.                                                                                                                                                                                              |

### Function Definitions
In `functions.py`, write the following 10 function definitions:

1. `get_total_experience()`:
   - **Input:** Accepts a single `Creature` object.
   - **Output:** Returns the integer value of the sum of the object's `resilience`, `courage`, `willpower`, and `determination` attributes.
2. `get_average_experience()`:
   - **Input:** Accepts a single `Creature` object.
   - **Output:** Returns the floating-point value of the average (mean) of the object's `resilience`, `courage`, `willpower`, and `determination` attributes.
   - **Other Requirement(s):** The return value must be a floating-point, not an integer.
3. `get_attribute()`:
   - **Input:** Accepts a single `Creature` object and a `str` value.
   - **Output:** Returns the value of the object's attribute corresponding to the given string. If the string does not match any of the four attributes, return an integer 0.
   - **Other Requirement(s):** Only account for the `resilience`, `courage`, `willpower`, and `determination` attributes. Ignore case in string comparisons. Do not use the built-in `getattr()` function.
4. `has_kind()`:
   - **Input:** Accepts a single `Creature` object and a `str` value.
   - **Output:** Returns `True` if the object's `kinds` list contains the given string, and `False` otherwise.
   - **Other Requirement(s):** Ignore case in string comparisons.
5. `get_names()`:
   - **Input:** Accepts a list of `Creature` objects.
   - **Output:** Returns a `list[str]` with values corresponding to each input object's `name` attribute.
   - **Other Requirement(s):** Do not modify the input list.
6. `filter_by_description()`:
   - **Input:** Accepts a list of `Creature` objects and a `str` value.
   - **Output:** Returns a list of objects from the input list with a `description` string containing the given string.
   - **Other Requirement(s):** Do not modify the input list. Ignore case in string comparisons.
7. `filter_by_kind()`:
   - **Input:** Accepts a list of `Creature` objects and a `str` value.
   - **Output:** Returns a list of objects from the input list with a `kinds` list containing the exact input string.
   - **Other Requirement(s):** Do not modify the input list. Ignore case in string comparisons.
   - **Hint(s):** Use your `has_kind()` function.
8. `filter_by_attribute_less_than()`:
   - **Input:** Accepts a list of `Creature` objects, a `str` value, and an `int` value.
   - **Output:** Returns a list of objects from the input list with the given attribute value **strictly less** than the given integer.
   - **Other Requirement(s):** Only account for the `resilience`, `courage`, `willpower`, and `determination` attributes. If an invalid string is given, treat each object's attribute value as 0. Do not modify the input list. Ignore case in string comparisons.
   - **Hint(s):** Use your `get_attribute()` function.
9. `filter_by_attribute_greater_than()`:
   - **Input:** Accepts a list of `Creature` objects, a `str` value, and an `int` value.
   - **Output:** Returns a list of objects from the input list with the given attribute value **strictly greater** than the given integer.
   - **Other Requirement(s):** Only account for the `resilience`, `courage`, `willpower`, and `determination` attributes. If an invalid string is given, treat each object's attribute value as 0. Do not modify the input list. Ignore case in string comparisons.
   - **Hint(s):** Use your `get_attribute()` function.
10. `get_most_experienced()`:
    - **Input:** Accepts a list of `Creature` objects.
    - **Output:** Returns the first object in the list with the highest sum total of the `resilience`, `courage`, `willpower`, and `determination` attributes. In case of a tie, return the first object found.
    - **Other Requirement(s):** If provided with an empty list, return `None`. Use `Creature` as the return type.
    - **Hint(s):** Use your `get_total_experience()` function.

For full credit, each function must have a one-sentence docstring detailing its purpose and return value. Additionally, ensure proper parameter and return type annotations.

### Example Function Calls

The following examples use the `CREATURES_RED` list, which contains creatures with the following information:

#### get_total_experience

```python
get_total_experience(CREATURES_RED[0]) # Dinospore
# Output: 365

get_total_experience(CREATURES_RED[1]) # Emberspark
# Output: 352

get_total_experience(CREATURES_RED[2]) # Ripplefin
# Output: 320
```

#### get_average_experience

```python
get_average_experience(CREATURES_RED[0]) # Dinospore
# Output: 91.25

get_average_experience(CREATURES_RED[1]) # Emberspark
# Output: 88.0

get_average_experience(CREATURES_RED[2]) # Ripplefin
# Output: 80.0
```

#### get_attribute

```python
get_attribute(CREATURES_RED[0], 'willpower') # Dinospore
# Output: 100

get_attribute(CREATURES_RED[1], 'RESilienCe') # Emberspark
# Output: 77

get_attribute(CREATURES_RED[2], 'bank account balance') # Ripplefin
# Output: 0
```

#### has_kind

```python
has_kind(CREATURES_RED[3], 'nature') # Slumberbug
# Output: True

has_kind(CREATURES_RED[3], 'DaRk') # Slumberbug
# Output: True

has_kind(CREATURES_RED[3], 'fire') # Slumberbug
# Output: False

has_kind(CREATURES_RED[3], 'candy corn') # Slumberbug
# Output: False
```

#### get_names

```python
get_names(CREATURES_RED[:3])
# Output: ['Dinospore', 'Emberspark', 'Ripplefin']

get_names(CREATURES_RED[3:6])
# Output: ['Slumberbug', 'Shadowgnome', 'Emberfox']

get_names(CREATURES_RED[6:])
# Output: ['Nightgale', 'Urania', 'Harvinger', 'Pearlificent']

get_names(CREATURES_RED[0:0])
# Output: []
```

#### filter_by_description

```python
get_names(filter_by_description(CREATURES_RED, 'small'))
# Output: ['Dinospore', 'Ripplefin', 'Slumberbug']

get_names(filter_by_description(CREATURES_RED, 'FrIeNdLy'))
# Output: ['Shadowgnome', 'Emberfox']

get_names(filter_by_description(CREATURES_RED, 'definitely not a pokemon'))
# Output: []
```

Note the usage of `get_names()`.

#### filter_by_kind

```python
get_names(filter_by_kind(CREATURES_RED, 'fire'))
# Output: ['Emberspark', 'Shadowgnome', 'Emberfox', 'Harvinger']

get_names(filter_by_kind(CREATURES_RED, 'WiNd'))
# Output: ['Nightgale', 'Urania']

get_names(filter_by_kind(CREATURES_RED, 'unkind'))
# Output: []
```

Note the usage of `get_names()`.

#### filter_by_attribute_less_than

```python
get_names(filter_by_attribute_less_than(CREATURES_RED, 'resilience', 90))
# Output: ['Emberspark', 'Ripplefin', 'Shadowgnome']

get_names(filter_by_attribute_less_than(CREATURES_RED, 'WiLlPoWeR', 100))
# Output: ['Emberspark', 'Slumberbug', 'Harvinger']

get_names(filter_by_attribute_less_than(CREATURES_RED, 'YouTube followers', 255))
# Treats each creature's non-existent "YouTube followers" attribute as 0
# I.e., each comparison is 0 < 255, which is always True
# Outputs a list of every creature's name from CREATURES_RED
```

Note the usage of `get_names()`.

#### filter_by_attribute_greater_than

```python
get_names(filter_by_attribute_greater_than(CREATURES_RED, 'determination', 210))
# Output: ['Shadowgnome', 'Nightgale', 'Urania', 'Harvinger']

get_names(filter_by_attribute_greater_than(CREATURES_RED, 'CoUrAgE', 200))
# Output: ['Urania']

get_names(filter_by_attribute_greater_than(CREATURES_RED, 'GPA', 4))
# Treats each creature's non-existent "GPA" attribute as 0
# I.e., each comparison is 0 > 4, which is always False
# Output: []
```

Note the usage of `get_names()`.

#### get_most_experienced()

```python
get_most_experienced(CREATURES_RED[:3]).name
# Output: 'Dinospore'

get_most_experienced(CREATURES_RED[3:6]).name
# Output: 'Slumberbug'

get_most_experienced(CREATURES_RED[6:]).name
# Output: 'Urania'

get_most_experienced(CREATURES_RED[0:0]) # Empty list
# Output: None
```

Note the usage of the dot operator and lack of list output.

### Unit Testing

In `function_tests.py`, write two unit tests for each of your 10 functions written in `functions.py`.

For each function, you must write at least one test case using the `CREATURES_BLUE` list and another using the large `CREATURES` list.

For functions 1-4, you can select a single creature from the respective list, e.g., `CREATURES_BLUE[3]`, for input into the function.

To more easily test list output values, please do the following:
- When testing `CREATURES_BLUE` as an input parameter, you can test `get_names()` of the output list, as in the example function calls.
  - When testing the larger `CREATURES` list, you can test the resulting `len()` of the output lists.

## Submission

Commit and push your changes to GitHub.

On Canvas, submit a screenshot of GitHub.com as evidence of your submission.

## Success Checklist
- [ ] Wrote the `Creature` class in `creatures.py`, outside of a main guard.
  - [ ] Includes a docstring
  - [ ] Wrote the `__init__` method.
    - [ ] Includes parameter and return type annotations
    - [ ] All listed attributes are initialized.
  - [ ] Wrote the `__str__` method
    - [ ] Includes parameter and return type annotations
    - [ ] String follows the exact format, including spaces and single quotation marks.
  - [ ] Wrote the `__eq__` method
    - [ ] Includes parameter and return type annotations
    - [ ] Properly checks all instance variables of both objects
  - [ ] Running `print_creatures.py` does not produce an error.
  - [ ] Wrote all 10 function definitions.
    - [ ] Each function definition includes a docstring.
    - [ ] Each function definition includes parameter and return type annotations.
    - [ ] The included tests using `CREATURES_RED` pass for each function.
    - [ ] Function definitions are not within a main guard.
  - [ ] Wrote two test cases for each function definition in `function_tests.py`.
    - [ ] Wrote a test case method that uses `CREATURES_BLUE` for each function definition.
    - [ ] Wrote a test case method that uses `CREATURES` for each function definition.
    - [ ] All test case methods are within the `FunctionTests(unittest.TestCase)` class.
  - [ ] All files were committed and pushed to GitHub.
    - [ ] `creature.py`
    - [ ] `function_tests.py`
    - [ ] `functions.py`
  - [ ] Your Canvas screenshot includes your repository name.
"""conditionals.py"""


def concatenate(cats: list[str], i: int) -> list[str]:
    concatenated = ""
    while i < len(cats):
        if cats[i] == 'pearl':
            i = i + 1
            continue
        concatenated = concatenated + cats[i] + ' '
        i = i + 1
    return concatenated


the_cats = ['mochi', 'harvest', 'pearl']

entire = concatenate(the_cats, 0)
partial = concatenate(the_cats, 1)

print("End of program.")

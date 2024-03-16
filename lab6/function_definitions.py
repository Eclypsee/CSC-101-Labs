"""function_definitions.py"""
from book import Book
def selection_sort_books(values:list[Book])->list[Book]:
    for i in range(len(values)):
        i_min = i
        value_min = values[i].title
        for j in range(i, len(values)):
            if values[j].title < value_min:  # Comparison
                i_min = j
                value_min = values[j].title
        # Swap
        values[i].title, values[i_min].title = values[i_min].title, values[i].title
    return values
def swap_case(input_str:str)->str:
    s = ''
    for i in input_str:
        if i.islower():
            s=s+i.upper()
        else:
            s=s+i.lower()
    return s
def str_translate(s:str, og:str, replacedwith:str)->str:
    out = ''
    for i in s:
        if i==og:
            out=out+replacedwith
        else: out=out+i
    return out

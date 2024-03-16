"""selection_sort.py"""

def selection_sort(values: list[int]) -> None:
    """Perform an in-place selection sort."""
    
    for i in range(len(values)):
        i_min = i
        value_min = values[i]
        for j in range(i, len(values)):
            if values[j] < value_min: # Comparison
                i_min = j
                value_min = values[j]
        
        # Swap
        temp = values[i]
        values[i] = values[i_min]
        values[i_min] = temp
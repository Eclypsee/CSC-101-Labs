def summation(numbers: list[int]) -> int:
    """Return the sum of all the numbers."""
    total = 0
    for k in range(len(numbers)):
        total = total + numbers[k]
    return total

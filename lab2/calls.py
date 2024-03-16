"""calls.py
A program that places several calls to the call stack at once.
"""


def calculate_distance(x_1: float, y_1: float, x_2: float, y_2: float) -> int:
    """Return the distance between two 2d-coordinates."""
    dx = x_2 - x_1
    dy = y_2 - y_1
    return (dx * dx + dy * dy) ** (0.5)


def calculate_magnitude(x: float, y: float) -> float:
    """Return the magnitude of a vector with the given x and y components"""
    magnitude = calculate_distance(0, 0, x, y)
    return magnitude


if __name__ == '__main__':
    result = calculate_magnitude(3.0, 4.0)
    print(result)

class Point:
    """Represent a point."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x:.2f}, {self.y:.2f})'

    def __str__(self):
        return repr(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __repr__(self) -> str:
        return f'(top_left={self.top_left}, bottom_right={self.bottom_right})'

    def __str__(self):
        return repr(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return self.top_left == other.top_left and self.bottom_right == other.bottom_right


class Circle:
    """Represents a circle."""

    def __init__(self, origin: Point, radius: float) -> None:
        self.origin = origin
        self.radius = radius

    def __repr__(self) -> str:
        return f'(origin={self.origin}, radius={self.radius:.2f})'

    def __str__(self):
        return repr(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return False
        return self.origin == other.origin and self.radius == other.radius

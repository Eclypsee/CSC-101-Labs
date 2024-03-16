"""book.py"""


class Book:
    """Represent a titled book written by a single author"""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

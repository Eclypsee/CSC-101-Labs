class Book:
    """Represent an authored book."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __repr__(self) -> str:
        return f'"{self.title}" by {self.author}'

    def __str__(self):
        return repr(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

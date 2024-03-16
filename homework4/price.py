class Price:
    """Represent a dollar and cents price."""

    def __init__(self, dollars: int, cents: int) -> None:
        self.dollars = dollars
        self.cents = cents

    def __repr__(self) -> str:
        return f'${self.dollars}.{self.cents:>02d}'

    def __str__(self):
        return repr(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Price):
            return False
        return self.dollars == other.dollars and self.cents == other.cents

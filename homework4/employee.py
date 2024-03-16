class Employee:
    """Represent a named and paid employee."""

    def __init__(self, name: str, pay: float) -> None:
        self.name = name
        self.pay = pay

    def __repr__(self) -> str:
        return f'(name={self.name}, pay={self.pay})'

    def __str__(self):
        return repr(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Employee):
            return False
        return self.name == other.name and self.pay == other.pay

"""creature.py"""


class Creature:
    """a creature class for a video game"""
    def __init__(self, number:int, name:str, kinds:list[str], height:float, weight:float, friendliness:int, resilience:int, courage:int, willpower:int, determination:int, legendary:bool, description:str)->None:
        self.number = number
        self.name = name
        self.kinds = kinds
        self.height = height
        self.weight = weight
        self.friendliness = friendliness
        self.resilience = resilience
        self.courage = courage
        self.willpower = willpower
        self.determination = determination
        self.legendary = legendary
        self.description = description
    def __str__(self)->str:
        return f"Creature(number={self.number}, name='{self.name}', kinds={self.kinds}, height={self.height}, weight={self.weight}, friendliness={self.friendliness}, resilience={self.resilience}, courage={self.courage}, willpower={self.willpower}, determination={self.determination}, legendary={self.legendary}, description='{self.description}')"
    def __eq__(self, other)->bool:
        if not isinstance(other, Creature):
            return False
        else:
            return self.number == other.number and self.name == other.name and self.kinds == other.kinds and self.height == other.height and self.weight == other.weight and self.friendliness == other.friendliness and self.resilience == other.resilience and self.courage == other.courage and self.willpower == other.willpower and self.determination == other.determination and self.legendary == other.legendary and self.description == other.description
c = Creature(0, 'a', ['b'], 1., 2., 1, 2, 3, 4, 5, False, 'c')

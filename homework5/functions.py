"""functions.py"""

from creature import Creature
from loader import CREATURES, CREATURES_RED, CREATURES_BLUE
def get_total_experience(c:Creature)->int:
    return c.resilience+c.courage+c.willpower+c.determination
def get_average_experience(c:Creature)->float:
    return (c.resilience+c.courage+c.willpower+c.determination)/4.0
def get_attribute(c:Creature, si:str)->int:
    s=si.lower()
    if s=="resilience":
        return c.resilience
    elif s == "courage":
        return c.courage
    elif s == "willpower":
        return c.willpower
    elif s == "determination":
        return c.determination
    else:
        return 0
def has_kind(c:Creature, s:str)->bool:
    for i in c.kinds:
        if i.lower() == s.lower():
            return True
    return False
def get_names(p:list[Creature])->list[str]:
    if len(p)>0:
        return [c.name for c in p if isinstance(c, Creature)]
    else:
        return []
def filter_by_description(p:list[Creature], s:str)->list[Creature]:
    return [a for a in p if s.lower() in a.description]
def filter_by_kind(p:list[Creature], s:str)->list[Creature]:
    return [a for a in p if s.lower() in a.kinds]
def filter_by_attribute_less_than(p:list[Creature], s:str, i:int)->list[Creature]:
    return [a for a in p if get_attribute(a, s)<i]
def filter_by_attribute_greater_than(p:list[Creature], s:str, i:int)->list[Creature]:
    return [a for a in p if get_attribute(a, s)>i]
def get_most_experienced(p:list[Creature])->Creature:
    if len(p)<1:
        return None
    max = p[0]
    for i in range(len(p)):
        if get_total_experience(p[i])>get_total_experience(max):
            max=p[i]
    return max




if __name__ == '__main__':
    print(f'len(CREATURES): {len(CREATURES)}')
    print(f'CREATURES_RED:  {CREATURES_RED}')
    print(f'CREATURES_BLUE: {CREATURES_BLUE}')

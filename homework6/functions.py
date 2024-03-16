"""functions.py"""
from creature import Creature


def list_to_creature(data: list[str]) -> Creature:
    """Returns the creature represented by a list of string data."""
    return Creature(
        int(data[0]),
        data[1],
        [i for i in [data[2], data[3]] if i],
        float(data[4]),
        float(data[5]),
        int(data[6]),
        int(data[7]),
        int(data[8]),
        int(data[9]),
        int(data[10]),
        data[11] == 'yes',
        data[12],
    )


def report_creature(creature: Creature) -> None:
    """Print out a creature's information in a pretty format."""
    print(creature.name)
    print(f'\tIDNO: {creature.number:0>3}')
    print(f'\tKIND: {creature.kinds}')
    print(f'\tHGHT: {creature.height:0>5.1f}')
    print(f'\tWGHT: {creature.weight:0>5.1f}')
    print(f'\tFRND: {creature.friendliness:0>3}')
    print(f'\tRESI: {creature.resilience:0>3}')
    print(f'\tCOUR: {creature.courage:0>3}')
    print(f'\tWILL: {creature.willpower:0>3}')
    print(f'\tLGND: {creature.legendary}')
    print(f'\tDESC: {creature.description}')


def load_creatures_text_file(file_path: str) -> list[Creature]:
    """Reads a text file to produce a list of Creature objects"""
    try:
        out = []
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line == '':
                    current = line.split(':')
                    # current[2:4] = [current[2:4]]
                    out.append(list_to_creature(current))
            return out
    except FileNotFoundError:
        print("File not found")




"""functions.py"""
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
    list_creatures = load_creatures_text_file('cscreatures.txt')
    for i in list_creatures:
        print(i)
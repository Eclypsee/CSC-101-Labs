"""loader.py
Loads all creature data into a list of Creature objects.

Requires a complete Creature class to function.
"""
import pickle
from creature import Creature


def load_creatures_as_lists() -> list[list[str]]:
    """Loads the binary data file containing a list of creatures, as lists."""
    with open('creatures.pkl', 'rb') as f:
        creatures = pickle.load(f)
    return creatures


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


try:
    CREATURES = [list_to_creature(creature_data) for creature_data in load_creatures_as_lists()]
    CREATURES_RED = [CREATURES[i] for i in [0, 3, 6, 14, 28, 100, 122, 143, 149, 150]]
    CREATURES_BLUE = [CREATURES[i] for i in [0, 3, 6, 12, 31, 102, 117, 144, 148, 150]]
except (SyntaxError, IndexError, ImportError, NameError):
    CREATURES = []
    CREATURES_RED = []
    CREATURES_BLUE = []

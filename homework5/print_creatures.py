"""print_creatures.py
Displays all creatures in the database.
"""
from loader import CREATURES, CREATURES_RED, CREATURES_BLUE

if __name__ == '__main__':
    print(f'# CREATURES_RED (Total: {len(CREATURES_RED)})')
    for creature in CREATURES_RED:
        print(f'\t{creature}')
    print()

    print(f'# CREATURES_BLUE (Total: {len(CREATURES_BLUE)})')
    for creature in CREATURES_BLUE:
        print(f'\t{creature}')
    print()

    print(f'# CREATURES (Total: {len(CREATURES)})')
    for creature in CREATURES:
        print(f'\t{creature}')
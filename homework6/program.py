"""program.py"""

import sys

from creature import Creature
from functions import *

if __name__ == '__main__':
    # Initializes the "database"
    db = []

    # Obtains the script file path **DO NOT** modify this line.
    file_path = input("File Path: ")

    # Below, you are suggested to do the following:
    # - Open the file given by the user.
    # - Iterate on each line in the file.
    # - Determine what operation is given, if any, by that line.
    # - Reassign 'db' to an updated value or display information using
    #   the relevant function.
    # - Handle possible errors using try/except.
    with open(file_path, 'r') as f:
        for line in f:
            # Handle other operations here
            # You'll likely want to strip and split the line
            # Included is a partially complete 'load' operation
            if line == 'load\n':
                db = load_creatures_text_file('cscreatures.txt')
                print(f'Loaded {len(db)} entries')
            line = line.strip()
            if line == 'report-creatures':
                for c in db:
                    report_creature(c)
            elif line == 'report-count':
                print(f'{len(db)} entries')
            elif line == 'report-avg-exp':
                avg_exp = 0.0
                if len(db)>0:
                    for c in db:
                        avg_exp = avg_exp+get_total_experience(c)
                    avg_exp = avg_exp/len(db)
                print(f'Experience Average: {round(float(avg_exp), 1)}')
            elif 'report-avg-attr' in line:
                line = line.split(':')
                avg_attr = 0.0
                if len(db)>0:
                    for c in db:
                        avg_attr = avg_attr+get_attribute(c, line[1])
                    avg_attr = avg_attr/len(db)
                print(f'{line[1]} Average: {round(avg_attr, 1)}')
            elif 'report-percent-by-kind' in line:
                line = line.split(':')
                total = 0.0
                if len(db)>0:
                    for c in db:
                        if has_kind(c, line[1]):
                            total=total+1.0
                    total = total/len(db)
                print(f'{round(total*100, 1)}% {line[1]}')
            elif 'filter-by-kind' in line:
                line = line.split(':')
                new = []
                if len(db)>0:
                    for c in db:
                        if has_kind(c, line[1]):
                            new.append(c)
                db = new
                print(f'Filtered to {len(db)} entries')
            elif 'filter-by-attr-lt' in line:
                line = line.split(':')
                new = []
                if len(db)>0:
                    new = filter_by_attribute_less_than(db, line[1], int(line[2]))
                db = new
                print(f'Filtered to {len(db)} entries')
            elif 'filter-by-attr-gt' in line:
                line = line.split(':')
                new = []
                if len(db)>0:
                    new = filter_by_attribute_greater_than(db, line[1], int(line[2]))
                db = new
                print(f'Filtered to {len(db)} entries')




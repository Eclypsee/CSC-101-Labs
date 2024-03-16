"""program.py
A simple program that will concatenate strings.
"""
cat = 'mochi'

cats = cat + 'harvest'

cats = cats + 'pearl'

cats = cats[5:]  # Slice notation. Truncates the first 5 characters.

print('End of Program')

# trace table?
# Line	    cat	            cats
# 4         'mochi'
# 6                      'mochiharvest'
# 8                      'mochiharvestpearl'
# 10                     'harvestpearl'
# 12


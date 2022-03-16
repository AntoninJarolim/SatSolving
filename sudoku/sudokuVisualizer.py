import math
import string

import numpy as np
values = []
with open("sudoku/sudoku_lengal.in", "r") as file:
# with open("sudoku/ez_sudoku.in", "r") as file:
    for line in file:
        values.append([int(num) for num in line.split()])


# sort values
print(values)
values = sorted(values, key=lambda x:x[2])
values = sorted(values, key=lambda x:x[1])
values = sorted(values, key=lambda x:x[0])
print(values)

# check duplicities
dupes = [x for n, x in enumerate(values) if x in values[:n]]
if len(dupes) != 0:
    print("DUPLICIT VALUES: \nDuplicitni vstupni hodnoty: ",  dupes)
    exit(1)

# check valid input (not 1 1 1 && 1 1 2)
deepCopy = [arr.copy() for arr in values]
first_two = [line for line in deepCopy if line.pop()]
dupes = [x for n, x in enumerate(first_two) if x in values[:n]]
if len(dupes) != 0:
    print("SAME PLACE, MULTIPLE VALUES: \nAt this positions: ",  dupes)
    exit(1)


print()
print("Pičo jak to je furt:")
print(values)

rows = np.arange(9) + 1
cols = np.arange(9) + 1

cur = values.pop(0)
for row in rows:
    for col in cols:
        if cur[0] == row and cur[1] == col:
            print(cur[2], end=" ")
            if len(values) == 0:
                exit(0)
            cur = values.pop(0)
        else:
            print("_", end=" ")
        if col % 3 == 0:
            print(" ", end="")
    if row % 3 == 0:
        print()
    print()

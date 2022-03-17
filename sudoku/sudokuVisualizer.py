import math
import string
import sys

import numpy as np

def digit_list(num):
    arr = []
    for digit in str(num):
        arr.append(int(digit))
    return arr

values = []
mode = sys.argv[1]

if mode == "-clause":
    with open(sys.argv[2], "r") as file:
        # with open("sudoku/ez_sudoku.in", "r") as file:
        for last_line in file:
            pass

    all = [int(num) for num in last_line.split()]
    all = all[110:]
    all = [n for n in all if n>0]
    for n in all:
        values.append(digit_list(n))


elif mode == "-input":
    with open(sys.argv[2], "r") as file:
        # with open("sudoku/ez_sudoku.in", "r") as file:
        for line in file:
            values.append([int(num) for num in line.split()])

else:
    print("ERROR\nVALID MODE NOT SPECIFIED")
    exit(99)


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



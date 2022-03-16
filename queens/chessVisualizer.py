import math
import string

import numpy as np

with open("queens.out", "r") as file:
    for last_line in file:
        pass

all = [int(num) for num in last_line.split()]

zero = all.pop()
if zero != 0:
    print("reading wrong input")
    exit(1)

last = len(all)
row_len = int(math.sqrt(last))

alphabet = []
for letter in string.ascii_uppercase:
    alphabet.append(letter)

print()
print("  ", end="")
for num in range(row_len):
    print(alphabet[num], end=" ")
print()


reshaped = np.array(all).reshape(row_len, row_len)

i = 0
for row in reshaped:
    print(alphabet[i], end=" ")
    i = i + 1
    for num in row:
        if num < 0:
            print("-", end=" ")
        else:
            print("X", end=" ")
    print()

import sys
import numpy as np

print("c Solving Sudoku")
print("c Created by sudoku.py script")
print("c which was writen by Antonin Jarolim")
print("c")

print("p cnf " + str(999-111) + " 3756") # TODO: calc this GUTLY

# functions
def end_it():
    print(0)

def end_with(str):
    print(str, end=" ")
    end_it()

def oneInArr(arr):
    for num in arr:
        print(num, end=" ")
    end_it()

def not_two_in_arr(arr):
    for num in arr[:]:
        arr = np.delete(arr, 0)
        for other in arr:
            print("-" + str(num) + " -" + str(other), end=" ")
            end_it()

def notTwoValuesAt(row, col):
    start = int(str(row) + str(col) + "0")
    one_pos_all_vals = np.arange(start, start + 10)
    oneInArr(one_pos_all_vals)
    not_two_in_arr(one_pos_all_vals)

def int3str(st, sec, third):
    return str(st) + str(sec) + str(third)

# functions ends here

# load input to array
input = []
with open("sudoku_lengal.in", "r") as file:
# with open("ez_sudoku.in", "r") as file:
    for line in file:
        input.append([int(num) for num in line.split()])

# create 9*9 rows*cols
rows = np.arange(9) + 1
cols = np.arange(9) + 1
vals = np.arange(9) + 1

print("c not 1 1 1 and 1 1 2")
for row in rows:
    for col in cols:
        notTwoValuesAt(row, col)


print("c existing values")
for val in input:
    end_with(int3str(val[0],val[1],val[2]))

print("c one val in row - not 1 1 1 and 1 2 1")
for row in rows:
    for val in vals:
        arr = []
        for col in cols:
            num = int3str(row, col, val)
            arr.append(int(num))
        not_two_in_arr(arr)
        oneInArr(arr)


print("c one val in col - not 1 1 1 and 1 2 1")
for row in rows:
    for val in vals:
        arr = []
        for col in cols:
            num = int3str(col, row, val) # here is difference
            arr.append(int(num))
        not_two_in_arr(arr)
        oneInArr(arr)

print("c one val in square - not 111 and 221")
square_positions = [11, 14, 17,
                   41, 44, 47,
                   71, 74, 77]

squares = []
for pos in square_positions:
    sq = []
    for row in range(0,3):
        for col in range(0,3):
            sq.append(pos + 10*row + col)
    squares.append(sq)

vals = np.arange(1, 10)
for square in squares:
    for value in vals:
        val_in_sq = []
        for pos in square:
            pos_arr = [digit for digit in str(pos)]
            num = int3str(pos_arr[0], pos_arr[1], value)
            val_in_sq.append(int(num))
        not_two_in_arr(val_in_sq)

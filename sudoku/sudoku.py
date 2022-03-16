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
with open("sudoku/sudoku_lengal.in", "r") as file:
# with open("sudoku/ez_sudoku.in", "r") as file:
    for line in file:
        input.append([int(num) for num in line.split()])

# create 9*9 rows*cols
rows = np.arange(9) + 1
cols = np.arange(9) + 1
vals = np.arange(9) + 1

# not 1 1 1 and 1 1 2
for row in rows:
    for col in cols:
        pass #notTwoValuesAt(row, col)

# existing values
for val in input:
    # print(int3str(val[0],val[1],val[2]), end="")
    pass # end_it()

# print one val in row - not 1 1 1 and 1 2 1
for row in rows:
    for val in vals:
        arr = []
        for col in cols:
            num = int3str(row, col, val)
            arr.append(int(num))
        not_two_in_arr(arr)
        oneInArr(arr)


# print one val in col - not 1 1 1 and 1 2 1
for row in rows:
    for val in vals:
        arr = []
        for col in cols:
            num = int3str(col, row, val)
            arr.append(int(num))
        not_two_in_arr(arr)
        oneInArr(arr)

# print one val in square


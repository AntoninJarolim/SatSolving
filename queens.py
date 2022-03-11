import sys
import math
import numpy as np

if len(sys.argv) < 2:
    print("Please specify numeric parameter for input N.")

N = int(sys.argv[1])
print("c Solving " + str(N) + " Queen problem")
print("c Created by queens.py script")
print("c which was writen by Antonin Jarolim")
print("c")


# Create diagonals
a = np.arange(1, N*N +1).reshape(N,N)
diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
diags = [n.tolist() for n in diags]

# Count number of pairs in each diagonal
diag_c = 0
for diag in diags:
    d_len = len(diag)
    if d_len > 1:
        diag_c += d_len * (d_len-1)/2 # formula to number of pairs in list

# Count pairs in rows and cols
row_c = ( N * (N-1)/2 ) * N + N
col_c = row_c

print("p cnf " + str(N) +" "+ str(int(row_c + col_c + diag_c)))
# functions


def end_it():
    print(0)


def oneInArr(arr):
    for num in arr:
        print(num, end=" ")
    end_it()


def not_two_in_arr(arr):
    for num in arr[:]:
        arr.pop(0)
        for other in arr:
            print("-" + str(num) + " -" + str(other), end=" ")
            end_it()
# functions end here


for row in range(1, N+1):
    a_list = list(range((row - 1) * N + 1, row * N + 1))
    oneInArr(a_list)
    not_two_in_arr(a_list)

for col in range(1, N+1):
    a_list = [i for i in range(col,N*N +1,N)]
    oneInArr(a_list)
    not_two_in_arr(a_list)

for diag in diags:
    not_two_in_arr(diag)

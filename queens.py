import sys

import numpy as np

if len(sys.argv) < 2:
    print("Please specify numeric parameter for input N.")

N = sys.argv[1]
print("c Solving " + N + " Queen problem")
print("c Created by queens.py script")
print("c which was writen by Antonin Jarolim")
print("c")
print("p cnf 1 2 \n")  # TODO: calc this gutly
N = int(N)


def endIt():
    print(0)


def oneInArr(arr):
    for num in arr:
        print(num, end=" ")
    endIt()


def notTwoInArr(arr):
    for num in arr[:]:
        arr.pop(0)
        for other in arr:
            print("-" + str(num) + " -" + str(other), end=" ")
            endIt()


for row in range(1, N+1):
    a_list = list(range((row - 1) * N + 1, row * N + 1))
    oneInArr(a_list)
    notTwoInArr(a_list)

for col in range(1, N+1):
    a_list = [i for i in range(col,N*N +1,N)]
    oneInArr(a_list)
    notTwoInArr(a_list)

a = np.arange(1, N*N +1).reshape(N,N)

diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]

# Now back to the original array to get the upper-left-to-lower-right diagonals,
# starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

# Another list comp to convert back to Python lists from numpy arrays,
# so it prints what you requested.
diags = [n.tolist() for n in diags]
for diag in diags:
    notTwoInArr(diag)
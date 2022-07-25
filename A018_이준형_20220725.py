#https://www.acmicpc.net/problem/1026
#Treasure 

import sys
import copy

input_N = int(sys.stdin.readline())

array_A = list(map(int, sys.stdin.readline().split()[:input_N]))
array_B = list(map(int, sys.stdin.readline().split()[:input_N]))

temp_A = copy.deepcopy(array_A)
temp_B = copy.deepcopy(array_B)

temp_B.sort()

B_index = []

for i in range(input_N):
    B_index.append(temp_B.index(array_B[i]))

    if temp_B.count(array_B[i]) >=2:
        temp_B[temp_B.index(array_B[i])] = None

temp_A.sort(reverse = True)

for i in range(input_N):
    array_A[i] = temp_A[B_index[i]]

result =0 

for i in range(input_N):
    result += array_A[i] * array_B[i]

print(result)
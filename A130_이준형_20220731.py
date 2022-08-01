# ZERO
# https://www.acmicpc.net/problem/10773

import sys

inputK = int(sys.stdin.readline())

sumList =[]

idx = 0
for i in range(inputK):
    sumList.append(int(sys.stdin.readline()))

    if idx == 0 and sumList[idx] == 0:
        sumList.pop(idx)
    elif sumList[idx] == 0:
        sumList.pop(idx-1)
        sumList.pop(idx-1)
        idx -= 1
    else:
        idx +=1

print(sum(sumList))
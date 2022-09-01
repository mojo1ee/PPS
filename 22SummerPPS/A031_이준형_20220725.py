# dividing chocolate
# https://www.acmicpc.net/problem/2163

import sys 

N, M = map(int, sys.stdin.readline().split())

#General Expression boils down to be the following 
totalCuts = N-1 + N*(M-1)

print(totalCuts)
# Rope
# https://www.acmicpc.net/problem/2217

import sys 

inputN = int(sys.stdin.readline())

rope = []
value = []

for i in range(inputN):
    rope.append(int(sys.stdin.readline()))

rope.sort(reverse = True)

for i in range(inputN):
    value.append(rope[i] * (i+1))

print(max(value))
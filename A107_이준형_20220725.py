# Easy Q (that's the title...)
# https://www.acmicpc.net/problem/1292

import sys 

sequenceGiven = [1]

position = 1 
while len(sequenceGiven) < 1000:
    if sequenceGiven.count(position) < position:
        sequenceGiven.append(position)
    else:
        position += 1

A, B = map(int, sys.stdin.readline().split())

print(sum(sequenceGiven[A-1:B]))

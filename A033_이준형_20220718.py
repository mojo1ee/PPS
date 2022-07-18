import sys

score = []

for i in range(5):
    temp = list(map(int,sys.stdin.readline().split()))
    score.append(sum(temp))

print(score.index(max(score))+1, max(score))
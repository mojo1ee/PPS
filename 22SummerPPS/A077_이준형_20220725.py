#Score Calculation
#https://www.acmicpc.net/problem/2822

import sys 
import copy

numOfQuestion = 8
listOfScore =[]

#take input()
for i in range(numOfQuestion):
    listOfScore.append(int(sys.stdin.readline()))

#sort 
tempScores = copy.deepcopy(listOfScore)
listOfScore.sort()

#print total points 
print(sum(listOfScore[-5:]))

#calculate Question num (+1 since Q num starts from 1 (not 0 like idx nums))
output = [tempScores.index(e)+1 for e in listOfScore[-5:]]
output.sort()
#print Qnum result 
print(*output, sep=" ")
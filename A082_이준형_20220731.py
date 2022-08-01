# sort by age 
# https://www.acmicpc.net/problem/10814

import sys 
import copy

numOfMembers = int(sys.stdin.readline())

memberList = []

for i in range(numOfMembers):
    memberList.append(sys.stdin.readline().strip().split())
    memberList[i][0] = int(memberList[i][0])
    memberList[i].insert(1,i)

keyPair = copy.deepcopy(memberList)
keyPair = [e[1:3] for e in keyPair]

memberList = [e[0:2] for e in memberList]
memberList.sort()

for i in range(numOfMembers):
    memberList[i][1] = keyPair[memberList[i][1]][1]

for member in memberList:
    print(member[0], member[1])
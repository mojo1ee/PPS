#https://www.acmicpc.net/problem/1157
#Vocab Study 

import sys 

ogString = sys.stdin.readline().strip()

tempString = ogString.lower()

alphaList =[]
alphaCount =[]
idx = 0

while len(tempString) > 0:

    alphaList.append(tempString[0])

    alphaCount.append(tempString.count(alphaList[idx]))

    tempString = [char for char in tempString if char != alphaList[idx]]

    idx += 1

maxFrequency = max(alphaCount)

if alphaCount.count(maxFrequency) > 1:
    print("?")
else:
    print(alphaList[alphaCount.index(maxFrequency)].upper())
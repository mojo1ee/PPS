#Group word checker
#https://www.acmicpc.net/problem/1316

import sys  

N = int(sys.stdin.readline())

numOfGroupWord = 0

for i in range(N):
    testWord = sys.stdin.readline().strip()
    
    uniqueChars = list(set(testWord))
    
    flag =0 

    for char in uniqueChars:
        if testWord.count(char) == 1:
            continue
        else:
            charIndexList = []

            for i in range(len(testWord)):
                if testWord[i] == char:
                    charIndexList.append(i)

            for i in range(len(charIndexList)):
                if i == 0:
                    prev = charIndexList[i]
                    continue

                if charIndexList[i] - prev != 1:
                    flag = 1 
                    break

                prev = charIndexList[i]

            if flag ==1:
                break 

    if flag != 1:
        numOfGroupWord += 1


print(numOfGroupWord)
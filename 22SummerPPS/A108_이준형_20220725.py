#reversing a number
#https://www.acmicpc.net/problem/3062

import sys 

numOfTestCases = int(sys.stdin.readline())

for i in range(numOfTestCases):
    testNum = sys.stdin.readline().strip()
    
    sumResult = int(testNum) + int(testNum[::-1])

    flag = 0
    for j in range(round(len(str(sumResult)) / 2)):
        if str(sumResult)[j] != str(sumResult)[-(j+1)]:
            print("NO")
            flag = 1
            break

    if flag == 0:
        print("YES")
#Door Door Door 
#https://www.acmicpc.net/problem/17210

import sys 

numOfDoors = int(sys.stdin.readline())

firstMethod = thirdMethod = int(sys.stdin.readline())
secondMethod = 1 if firstMethod == 0 else 0

if numOfDoors >= 6:
    print("Love is open door")
else:
    for i in range(numOfDoors-1):
        if (i+2) % 2 == 0:
            print(secondMethod)
        elif (i+2) % 3 == 0: 
            print(thirdMethod)
        else:
            print(thirdMethod)
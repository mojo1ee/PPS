# sorting w/o duplicates 
# https://www.acmicpc.net/problem/10867

import sys 

#Receive Input 
numOfInput =  int(sys.stdin.readline())
listOfInput = list(map(int, sys.stdin.readline().split()[:numOfInput]))

#Sort out unique elements and sort 
setOfInput = set(listOfInput)
listOfInput = list(setOfInput)
listOfInput.sort()

#Print Out
print(*listOfInput, sep = ' ')
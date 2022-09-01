# sort all suffixes 
# https://www.acmicpc.net/problem/11656

import sys
import copy 

stringInput = sys.stdin.readline().strip()

tempString = copy.deepcopy(stringInput)

suffixList = [] 

for i in range(len(stringInput)):
    suffixList.append(tempString[i:len(tempString)])

suffixList.sort()

for item in suffixList:
    print (item)
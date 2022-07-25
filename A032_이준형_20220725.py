#https://www.acmicpc.net/problem/2775
#town hall president 

import sys

numOfCases = int(sys.stdin.readline())

for i in range(numOfCases):
    floor_k = int(sys.stdin.readline()) #for floors (ranges from 0(0th floor), 1<=k) 
    room_n = int(sys.stdin.readline()) #for room_no (ranges from ) 1<=14 (but index wise 0~13)

    residents =[]

    for j in range(floor_k):
        if j != 0:
            residents.append([sum(residents[j-1][:idx+1]) if idx > 0 else 1 for idx in range(room_n)])
        elif j == 0:
            residents.append(list(range(1,room_n+1)))
        
    print(sum(residents[floor_k-1]))
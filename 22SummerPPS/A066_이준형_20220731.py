#https://www.acmicpc.net/problem/1427
#Sort inside 


import sys

n = int(sys.stdin.readline())
 
listForSorting = []
for i in str(n):
    listForSorting.append(int(i))
    
listForSorting.sort(reverse = True)
 
for i in listForSorting:
    print(i, end = '')

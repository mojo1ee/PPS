#Cards 2 
#https://www.acmicpc.net/problem/2164

import sys 
from collections import deque

inputN = int(sys.stdin.readline())
deque = deque([i for i in range(1, inputN+1)])

while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])
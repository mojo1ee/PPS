# Fibonacci 
# https://www.acmicpc.net/problem/4150

import sys  

n = int(sys.stdin.readline())

fibonacci = [0, 1]

for i in range(2, n+1):
    num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(num)
    
print(fibonacci[n])
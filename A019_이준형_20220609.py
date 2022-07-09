'''https://www.acmicpc.net/problem/2577
'''

A = int(input())
B = int(input())
C = int(input())
    
product = A*B*C
product = str(product)
    
for i in range(10):
    print(product.count(str(i)))
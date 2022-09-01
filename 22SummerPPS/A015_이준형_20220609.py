#https://www.acmicpc.net/problem/2475

code = list(map(int, input().split()))

sum = 0

for i in range(5):
    sum += (code[i] * code[i])
    
print(sum%10)
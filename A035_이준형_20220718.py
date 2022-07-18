#https://www.acmicpc.net/problem/5355

import sys

numberOfCases = int(sys.stdin.readline())

for i in range(numberOfCases):
    equation = list(sys.stdin.readline().split())

    answer = float(equation[0])

    for j in range(len(equation)-1):
        if equation[j+1] == '@':
            answer *= 3
        elif equation[j+1] == '%':
            answer += 5
        elif equation[j+1] == '#':
            answer -= 7

    print(f'{answer:.2f}')
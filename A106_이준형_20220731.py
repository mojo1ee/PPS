# sum of excluded alphabets 
# https://www.acmicpc.net/problem/3059

import sys

numOfTestCases = int(sys.stdin.readline())

capitalAlphabetList = [chr(i) for i in range(65,91)]

for i in range(numOfTestCases):
    testCase = sys.stdin.readline().strip()
    testCase = list(set(testCase))

    momentOfTruth = [ord(a) for a in capitalAlphabetList if a not in testCase]
    print(sum(momentOfTruth))
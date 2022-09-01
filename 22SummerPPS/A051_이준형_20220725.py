# Dial
# https://www.acmicpc.net/problem/5622

import sys 

word = sys.stdin.readline().strip()

wordGroup = [['A','B','C'],['D','E','F'],['G','H','I'],
             ['J','K','L'],['M','N','O'],['P','Q','R','S'],
             ['T','U','V'], ['W','X','Y','Z']]
seconds = 0

for letter in word:
    for i in range(len(wordGroup)):
        if letter in wordGroup[i]:
            seconds += (i+3)

print(seconds)
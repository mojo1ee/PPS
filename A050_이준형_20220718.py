#https://www.acmicpc.net/problem/5598

import sys

inputString = sys.stdin.readline().strip()

ogString = [chr(((ord(char)-3))) if ord(char) > 67 else chr(90-(abs(ord(char)-67))) for char in inputString]

print(''.join(ogString))
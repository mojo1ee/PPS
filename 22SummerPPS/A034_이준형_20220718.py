#https://www.acmicpc.net/problem/3052

import sys

num_list = []

for i in range(10):
    num_list.append(int(sys.stdin.readline()) % 42)

final_list = []

for num in num_list:
    if num not in final_list:
        final_list.append(num)

print(len(final_list)) 
#https://www.acmicpc.net/problem/2010

import sys

n_strip = int(input())
n_outlets = []

for i in range(n_strip):
    n_outlets.append(int(sys.stdin.readline()))
    
n_appliance = 0

for i in range(len(n_outlets)):
    if i!=0:
        n_appliance -=1

    n_appliance +=n_outlets[i]

print(n_appliance)
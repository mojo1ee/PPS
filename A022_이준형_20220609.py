#https://www.acmicpc.net/problem/1267

import sys

n_calls = int(sys.stdin.readline())

call_time = list(map(int, sys.stdin.readline().split()))[:n_calls]

total_bill_Y = 0
total_bill_M = 0

for time in call_time:

    if time > 0:
        bill_Y = 10
        bill_M = 15 
    
    bill_Y += (time//30)*10
    
    if time - ((time//30)*30) > 29:
        bill_Y += 10
        
    total_bill_Y += bill_Y
    
    bill_M += (time//60)*15
    
    if time - ((time//60)*60) > 59:
        bill_M += 15
        
    total_bill_M += bill_M
    
if total_bill_Y < total_bill_M:
    print("Y",total_bill_Y)
    
elif total_bill_M < total_bill_Y:
    print("M",total_bill_M)
    
else:
    print("Y M",total_bill_Y)
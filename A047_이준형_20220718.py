#https://www.acmicpc.net/problem/11721
import sys

string = sys.stdin.readline().strip()

temp_string  = ''

for i in range(len(string)):
    
    temp_string += string[i]
    
    if ((i+1) % 10) == 0 or i == (len(string)-1):
        
        print(temp_string)
            
        temp_string = ''
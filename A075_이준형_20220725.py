#Biggest Number
#https://school.programmers.co.kr/learn/courses/30/lessons/42746

import sys

def solution(numbers):
    
    #change elements in list "numbers" in to str
    numbers = list(map(str,numbers))
    
    #match digits(=3) with *3 (<=1000)
    #reverse = True b.c of str (ASCII) properties 
    numbers.sort(key=lambda x: x*3, reverse = True)
    
    #add a layer of int() b.c of cases that involve only 0's
    return str(int(''.join(numbers)))
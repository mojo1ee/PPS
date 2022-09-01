#https://school.programmers.co.kr/learn/courses/30/lessons/12947
#하샤드 수

def solution(x):
    answer = True
    
    str_x = str(x)
    list_x = []
    
    for letter in str_x:
        list_x.append(int(letter))
    
    divisor = sum(list_x)
    
    if x%divisor != 0:
        return False
    
    return answer
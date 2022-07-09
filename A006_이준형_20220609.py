'''
문자열 내 p와 y의 개수
https://school.programmers.co.kr/learn/courses/30/lessons/12916
'''

def solution(s):
    answer = True
    
    count_p = 0 
    count_y = 0
    
    for letter in s:
        if letter == 'p' or letter == 'P':
            count_p += 1
        elif letter == 'y' or letter == 'Y':
            count_y += 1 
            
    if count_p != count_y:
        answer = False

    return answer
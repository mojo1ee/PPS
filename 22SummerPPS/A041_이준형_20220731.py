#https://school.programmers.co.kr/learn/courses/30/lessons/12951
#JadenCase

def solution(s):
    
    
    s1 = s.lower()
    answer = ''
    
    idx = -1
    for i in range(len(s1)):
        
        currentChar = s1[i]
        
        if currentChar == " ":
            idx = -1 
            answer = answer + currentChar
            continue
        else:
            idx += 1
        
        if idx == 0:
            if 97 <= ord(currentChar) <= 122:
                answer = answer + currentChar.upper()
            else:
                answer = answer + currentChar
        else:
            answer = answer + currentChar
        
        
    return answer
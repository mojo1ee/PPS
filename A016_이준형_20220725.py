#https://school.programmers.co.kr/learn/courses/30/lessons/42885
#life boat 

def solution(people, limit):
    
    people.sort()

    #two pointer algorithm
    
    i, j = 0, len(people) -1
    
    answer = 0
    
    while i <= j:
        
        if people[i] + people[j] > limit:
            j -= 1
        else:
            i += 1
            j -= 1
            
        answer += 1
    
    return answer
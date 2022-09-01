#https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)):
        flag = True
        idx = 0
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                if skill_trees[i][j] == skill[idx]:
                    idx += 1
                else:
                    flag = False
                    break
        if flag:
            answer += 1

    return answer
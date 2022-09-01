#https://www.acmicpc.net/problem/4344

test_cases = int(input())

for test in range(test_cases):
    case = list(map(int,input().split()))
    
    case_avg = sum(case[1:])/len(case[1:])
    
    over_avg = 100 * len([x for x in case[1:] if x > case_avg])/case[0]
    
    print('%.3f' % over_avg + "%")
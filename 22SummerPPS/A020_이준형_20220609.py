#https://www.acmicpc.net/problem/2455

p_current = 0
p_max =0

for i in range(4):
    p_out, p_in = map(int, input().split())

    p_current -= p_out

    p_max = p_max if p_max > p_current else p_current

    p_current += p_in

    p_max = p_max if p_max > p_current else p_current

print(p_max)
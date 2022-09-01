#Good Day Bad Day
#https://www.acmicpc.net/problem/17211

import sys 

nDays, currentMood = map(int,sys.stdin.readline().split())

fourDayForecast = list(map(float, sys.stdin.readline().split()))

probGood = [0]
probBad = [0]

if currentMood == 0:
    probGood[0] = fourDayForecast[0]
    probBad[0] = fourDayForecast[1]
else:
    probGood[0] = fourDayForecast[2]
    probBad[0] = fourDayForecast[3]

for i in range(nDays -1):
    probGood.append(probGood[i]*fourDayForecast[0] + probBad[i]*fourDayForecast[2])
    probBad.append(probGood[i]*fourDayForecast[1] + probBad[i]*fourDayForecast[3])

print(round(probGood[-1] * 1000))
print(round(probBad[-1] * 1000))
# Cheapest Fare 
# https://www.acmicpc.net/problem/14487

import sys

numOfVillages = int(sys.stdin.readline())

listOfFare = list(map(int,sys.stdin.readline().split()))[:numOfVillages]

listOfFare.remove(max(listOfFare))

print(sum(listOfFare))
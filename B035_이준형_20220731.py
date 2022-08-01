# Coin 0
# https://www.acmicpc.net/problem/11047

import sys 

kindOfCoinsN, desiredAmountK = map(int, sys.stdin.readline().split())

listOfCoins = []

for i in range(kindOfCoinsN):
    listOfCoins.append(int(sys.stdin.readline()))

listOfCoins = listOfCoins[::-1]
numOfCoinsNeeded = 0

for coin in listOfCoins:
    numOfCoinsNeeded += desiredAmountK // coin
    desiredAmountK %= coin

print(numOfCoinsNeeded)
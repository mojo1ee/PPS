# Change
# https://www.acmicpc.net/problem/5585

import sys 

coins = [500, 100, 50, 10, 5, 1]

payment = int(sys.stdin.readline())
change = 1000 - payment

nCoins = 0

for coin in coins:

    nCoins += change // coin
    change = change % coin

print(nCoins)
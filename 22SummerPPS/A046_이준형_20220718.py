#https://www.acmicpc.net/problem/1159
import sys

fullRoster = []

numberOfPlayers = int(sys.stdin.readline())

for i in range(numberOfPlayers):
    temp = sys.stdin.readline().strip()
    fullRoster.append(temp[0])

finalRoster =[]

while len(fullRoster)> 0:
    if fullRoster.count(fullRoster[0]) >= 5:
        finalRoster.append(fullRoster[0])
    
    fullRoster = [player for player in fullRoster if player != fullRoster[0]]

finalRoster.sort()

if len(finalRoster) > 0:
    print(''.join(map(str,finalRoster)))
else:
    print("PREDAJA")
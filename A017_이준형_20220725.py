#https://www.acmicpc.net/problem/1475
#RoomNO

import sys

roomNo = int(sys.stdin.readline())
roomNo = list(str(roomNo))

#first try to count each number from 0~9. 
#each number(idx) count from 0~9
numberCountList =[] 
for i in range(10):
    numberCountList.append(roomNo.count(str(i)))

#get sets needed for 6&9 combined
countFor69 = (numberCountList[6] + numberCountList[9])
if (countFor69 / 2) - (countFor69 //2) == 0:
    countFor69 = int(countFor69/2)
elif (countFor69 / 2) - (countFor69 //2) == 0.5:
    countFor69 = int(countFor69/2 + 0.5)

#get sets needed (maxSin69) w/o counting 6 and 9
numberCountList = numberCountList[0:6] + numberCountList[7:9]
maxSin69 = max(numberCountList)

if countFor69 >= maxSin69:
    print(countFor69)
else:
    print(maxSin69)
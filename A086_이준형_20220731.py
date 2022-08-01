# Numbers Play 
# https://www.acmicpc.net/problem/1755

import sys 

M, N = map(int, sys.stdin.readline().split())

listOfNumbers = []

for i in range(M, N+1):
    listOfNumbers.append(list(str(i)))


for item in listOfNumbers:
    for i in range(len(item)):
        if item[i] == "1":
            item[i] = "one"
        elif item[i] == "2":
            item[i] = "two"
        elif item[i] == "3":
            item[i] = "three"
        elif item[i] == "4":
            item[i] = "four"
        elif item[i] == "5":
            item[i] = "five"
        elif item[i] == "6":
            item[i] = "six"
        elif item[i] == "7":
            item[i] = "seven"
        elif item[i] == "8":
            item[i] = "eight"
        elif item[i] == "9":
            item[i] = "nine"
        elif item[i] == "0":
            item[i] = "zero"

#join within the embedded single list 
for i in range(len(listOfNumbers)):
    listOfNumbers[i] = " ".join(listOfNumbers[i])

#sort 
listOfNumbers.sort()

#convert back to separated elements within list 
for i in range(len(listOfNumbers)):
    listOfNumbers[i] = listOfNumbers[i].split()


#convert letter to number 
for item in listOfNumbers:
    for i in range(len(item)):
        if item[i] == "one":
            item[i] = "1"
        elif item[i] == "two":
            item[i] = "2"
        elif item[i] == "three":
            item[i] = "3"
        elif item[i] == "four":
            item[i] = "4"
        elif item[i] == "five":
            item[i] = "5"
        elif item[i] == "six":
            item[i] = "6"
        elif item[i] == "seven":
            item[i] = "7"
        elif item[i] == "eight":
            item[i] = "8"
        elif item[i] == "nine":
            item[i] = "9"
        elif item[i] == "zero":
            item[i] = "0"

#use "".join() to remove space in between 
for i in range(len(listOfNumbers)):
    listOfNumbers[i] = "".join(listOfNumbers[i])


#print according to format
#10 per line and then newline. 
for item in listOfNumbers:
    print(item, end=" ")
    if (listOfNumbers.index(item) +1) % 10 == 0 or listOfNumbers.index(item) == len(listOfNumbers) -1:
        print()
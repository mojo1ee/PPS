#Readable Password
#https://www.acmicpc.net/problem/4659

import sys 

testPassword = ''
while(testPassword != 'end'):
    testPassword = sys.stdin.readline().strip()

    # Need to include at least one vowel (a,e,i,o,u)
    if testPassword.count('a') + testPassword.count('e') \
    + testPassword.count('i') + testPassword.count('o') + testPassword.count('u') < 1:
        print("<"+testPassword+">", "is not acceptable.")
        continue

    prevChar =''
    prevType = -1

    sameCharCount = 1
    sameTypeCount = 1
    
    isVowel = -1
    flag = 0 

    for char in testPassword:

        #consecutive char count
        if prevChar == char:
            sameCharCount += 1
        else:
            sameCharCount = 1 

        #consecutive vowel/consonant count
        if char in ['a','e','i','o','u']:
            isVowel =  1
        else:
            isVowel = 0

        if prevType == isVowel:
            sameTypeCount += 1
        else:
            sameTypeCount = 1 

        # vowels/consonants cannot appear 3 times in a row
        if sameTypeCount >=3:
            flag = 1
            break

        # two same consecutive characters not allowed except "ee" and "oo"
        if sameCharCount >= 3:
            flag =1 
            break
        elif sameCharCount >= 2:
            if char not in ["e","o"]:
                flag = 1
                break
            
        prevChar = char
        prevType = isVowel
    
    if flag == 1 and testPassword != "end":
        print("<"+testPassword+">", "is not acceptable.")
    elif flag == 0 and testPassword != "end":
        print("<"+testPassword+">", "is acceptable.")
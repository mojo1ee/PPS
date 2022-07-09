#Baekjoon 2920

numbers = list(map(int, input().split()))

answer = "mixed"

if numbers == sorted(numbers):
    answer = "ascending"
elif numbers == sorted(numbers, reverse = True):
    answer = "descending"
else:
    answer = "mixed"

print(answer)
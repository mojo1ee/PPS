import sys 

numOfArticles, ImpactFactorGoal = map(int, sys.stdin.readline().split())

needToBribe = numOfArticles * (ImpactFactorGoal-1) + 1;

print(needToBribe);

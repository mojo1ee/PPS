#include <stdio.h>
#define MAX_COINS 10

int main(){

    int numCoins;
    int moneyAmount;
    int change[MAX_COINS];
    int minNum = 0;

    scanf("%d", &numCoins);
    scanf("%d", &moneyAmount);

    for(int i = 0; i < numCoins; i++){
        scanf("%d", &change[i]);
    }

    while(moneyAmount > 0){
        for(int i = numCoins - 1; i >= 0; i--){
            minNum += moneyAmount / change[i];
            moneyAmount %= change[i];
        }
    }
    printf("%d\n", minNum);
    
    return 0;
}
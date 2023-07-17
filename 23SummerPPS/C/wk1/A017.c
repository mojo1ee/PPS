#include <stdio.h>

int main(){
    
    int numSet[9];
    for(int i = 0; i < sizeof(numSet) / sizeof(numSet[0]); i++){
        numSet[i] = 0;
    }

    int inputNum, quotient, remainder;
    scanf("%d", &inputNum);

    while(1){
        remainder = inputNum % 10;
        if(remainder == 9){
            numSet[6]++;
        }
        else numSet[remainder]++;

        quotient = inputNum / 10;
        if(quotient == 0) break;
        inputNum = quotient;
    }
    numSet[6] = (numSet[6] / 2) + (numSet[6] % 2);

    int max = 0;
    for(int i = 0; i < sizeof(numSet) / sizeof(numSet[0]); i++){
        if(numSet[i] > max) max = numSet[i];
    }
    printf("%d\n", max);

    return 0;
}
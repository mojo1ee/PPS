#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = false;
    
    int remainder;
    int sum = 0;
    int num = x;
    
    do{
        remainder = num % 10;
        sum += remainder; 
        num /= 10;
    }while(num != 0);
    
    if(x % sum == 0){
        return true;
    }

    return answer;
}

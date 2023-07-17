#include <stdio.h>

int main(){

    long int numDoors;
    int prevMethod;

    scanf("%ld", &numDoors);
    scanf("%d", &prevMethod);
    
    //secondMethod =  (firstMethod == 0) ?  1 : 0;

    if(numDoors >= 6){
        printf("Love is open door\n");
    }
    else{
        for(int i = 2; i <= numDoors; i++){
            if(prevMethod == 0){
                printf("%d\n", 1);
                prevMethod = 1;
            }
            else{
                printf("%d\n", 0);
                prevMethod = 0;
            }
        }
    }

    return 0;
}
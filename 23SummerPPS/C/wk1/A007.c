#include <stdio.h>
#include <stdlib.h>
#define NUM_NOTES 8

int main(){

    int i;
    int notes[NUM_NOTES];
    for(i = 0; i < NUM_NOTES; i++){
        scanf("%d", &notes[i]);
    }

    int indicator = 0; // -1 descending 1 is ascending
    int initial = 0;
    int prev;

    for(i = 0; i < NUM_NOTES; i++){
        if(i == 0) {
            prev = notes[i];
            continue;
        }

        if(prev < notes[i]){
            indicator = 1;
        }
        else if (prev > notes[i]){
            indicator = -1;
        }
        prev = notes[i];

        if(i == 1){
            initial = indicator;
            continue;
        }

        if(indicator != initial){
            indicator = 0;
            break;
        }
    }

    if(indicator == 0){
        printf("mixed\n");
    }
    else if(indicator == -1){
        printf("descending\n");
    }
    else if (indicator == 1){
        printf("ascending\n");
    }
    
    return 0;
}

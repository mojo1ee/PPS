#include <stdio.h>
#define NUM_STATION 4

int main(){

	int total = 0;
	int max = 0;
	int on, off;

	for(int i = 0; i < NUM_STATION; i++){
		scanf("%d %d", &off, &on);
		total = total - off + on;
		if(total > max){
			max = total;
		}
	}
	printf("%d\n", max);

	return 0;
}
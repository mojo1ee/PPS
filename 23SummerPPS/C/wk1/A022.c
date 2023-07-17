#include <stdio.h>

int main(){

	int numCalls, callTime;
	scanf("%d", &numCalls);

	int billM = 0;
	int billY = 0;

	for(int i = 0; i < numCalls; i++){
		scanf("%d", &callTime);

		billY += (callTime / 30) + 1;
		billM += (callTime / 60) + 1;
	}
	billY *= 10;
	billM *= 15;

	if(billY == billM){
		printf("Y M %d\n", billY);
	}
	else if(billY < billM){
		printf("Y %d\n", billY);
	}
	else{
		printf("M %d\n", billM);
	}

	return 0;
}
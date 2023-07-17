#include <stdio.h>

int main(){

	int serial[5];
	int sum = 0;
	int lastDigit;

	for(int i = 0; i < sizeof(serial)/sizeof(serial[0]); i++){
		scanf("%d", &serial[i]);
		sum += (serial[i] * serial[i]);
	}
	lastDigit = sum % 10;
	printf("%d\n", lastDigit);

	return 0;
}
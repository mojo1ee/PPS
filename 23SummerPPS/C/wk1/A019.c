#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

	//testing int max 2147483647
	//int product = 999 * 999 * 999;
	//printf("%d\n", product);

	int num1, num2, num3;
	scanf("%d", &num1);
	scanf("%d", &num2);
	scanf("%d", &num3);
	
	char str[10];
	int product = num1 * num2 * num3;
	sprintf(str, "%d", product);

	int digit = 0;
	int count;
	while(digit < 10){
		count = 0;
		for(int i = 0; i < strlen(str); i++){
			if(str[i] == digit + '0' ){
				count++;
			}
		}
		printf("%d\n", count);
		digit++;
	}
	return 0;
}
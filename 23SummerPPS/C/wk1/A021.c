#include <stdio.h>

int main(){

	int numCable, totalPorts = 0, numPorts = 0;
	scanf("%d", &numCable);

	for(int i = 0; i < numCable; i++){
		
		scanf("%d", &numPorts);
		if(i == 0){
			totalPorts = numPorts;
			continue;
		}
		totalPorts = totalPorts + numPorts - 1;
	}
	printf("%d\n", totalPorts);

	return 0;
}
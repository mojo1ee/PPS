int singleNumber(int* nums, int numsSize){

    int temp;
    int check;
    for(int i = 0; i < numsSize; i ++){
        temp = nums[i];
        check = 0;
        for(int j = 0; j < numsSize; j++){
            if(j == i) continue;
            if(temp == nums[j]) {
                check = 1;
                break;
            }
        }
        if(check == 0){
            return temp;
        }
    }
    return nums[numsSize - 1];
}
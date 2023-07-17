int addDigits(int num){
    int sum;

    do{
        sum = 0;
        do{
            sum += num % 10;
            num /= 10;
        }while(num != 0);
        num = sum;
    }while(sum >= 10);

    return sum;
}
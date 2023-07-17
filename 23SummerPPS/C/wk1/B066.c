void reverseString(char* s, int sSize){
    int front = 0;
    int rear = sSize - 1;
    int temp;

    while(front < rear){
        temp = s[front];
        s[front] = s[rear];
        s[rear] = temp;
        front++;
        rear--;
    }
}
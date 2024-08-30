#include<stdio.h>
#include<stdlib.h>

//defining the size of the arrayyyyy
#define SIZE 100


//defining the structure
struct stack {
    int info;
};

struct stack s[SIZE];
int top = -1;

  
//adding operations  
void push(int);
void pop();
void disp();

int main() {
    int ch, item;
    
        while (1) {
        printf("1-push\n");
        printf("2-pop\n");
        printf("3-display\n");
        printf("4-exit\n\n\n");
        printf("Enter your choice: ");
        scanf("%d", &ch);
// to choose the operation
        switch (ch) {
            case 1:
                printf("Enter a number: ");
                scanf("%d", &item);
                push(item);
                break;
            case 2:
                pop();
                break;
            case 3:
                disp();
                break;
            case 4:
                exit(0);
            default:
                printf("Sorry, no such operation.\n");
                break;
        }
    }
    return 0; // Return from main
}

//push operation
void push(int x) {
    if (top >= SIZE - 1) {
        printf("Stack is full and can cause overflow\n\n");
    } else {
        top++;
        s[top].info = x;
    }
}

//pop operation
void pop() {
    if (top == -1) {
        printf("Stack is empty and can cause underflow\n");
    } else {
        printf("The deleted item is %d\n\n", s[top].info);
        top--;
    }
}

//display operation
void disp() {
    if (top == -1) {
        printf("Stack is empty\n\n");
    } else {
        for (int i = top; i >= 0; i--) {
            printf("%d ", s[i].info);
        }
        printf("\n\n");
    }
}


// output
// 1-push
// 2-pop
// 3-display
// 4-exit


// Enter your choice: 1
// Enter a number: 23
// 1-push
// 2-pop
// 3-display
// 4-exit


// Enter your choice: 1
// Enter a number: 32
// 1-push
// 2-pop
// 3-display
// 4-exit


// Enter your choice: 2
// The deleted item is 32

// 1-push
// 2-pop
// 3-display
// 4-exit


// Enter your choice: 3
// 23 

// 1-push
// 2-pop
// 3-display
// 4-exit


// Enter your choice: 4
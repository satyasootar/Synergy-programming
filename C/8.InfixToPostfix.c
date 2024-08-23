#include <stdio.h>
#include <ctype.h>

char stack[20];
int top = -1;

void push(char x){
    stack[++top] = x;
}

char pop(){
    if(top == -1)
        return '\0';  // Use '\0' for empty stack
    else
        return stack[top--];
}

int priority(char x){
    switch(x){
        case '(': return 0;
        case '+':
        case '-': return 1;
        case '*':
        case '/': return 2;
        case '^': return 3;
        default: return -1;
    }
}

int main(){
    char exp[20];
    char *e;
    char x;

    printf("Enter the expression: ");
    scanf("%s", exp);

    e = exp;  // Initialize the pointer

    while(*e != '\0'){  // Use '\0' to check end of string
        if(isalnum(*e)){
            printf("%c", *e);  // Print operand
        }
        else if(*e == '('){
            push(*e);  // Push '(' onto stack
        }
        else if(*e == ')'){
            while((x = pop()) != '(')  // Pop until '(' is found
                printf("%c", x);
        }
        else {  // Operator case
            while(top != -1 && priority(stack[top]) >= priority(*e)){
                printf("%c", pop());
            }
            push(*e);
        }
        e++;
    }

    // Pop remaining operators from the stack
    while(top != -1){
        printf("%c", pop());
    }

    printf("\n");
    return 0;
}

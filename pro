#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100
struct Stack {
    int arr[MAX_SIZE];
    int top;
};
void initialize(struct Stack *stack) {
    stack->top = -1;
}
int isFull(struct Stack *stack) {
    return stack->top == MAX_SIZE - 1;
}
int isEmpty(struct Stack *stack) {
    return stack->top == -1;
}
void push(struct Stack *stack, int value) {
    if (isFull(stack)) {
        printf("Stack overflow\n");
        return;
    }
    stack->arr[++stack->top] = value;
    printf("%d pushed to stack\n", value);
}
int pop(struct Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack underflow\n");
        return -1;
    }
    return stack->arr[stack->top--];
}
int peek(struct Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack->arr[stack->top];
}
int main() {
    struct Stack stack;
    initialize(&stack);
    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);
    printf("Top element: %d\n", peek(&stack));
    printf("%d popped from stack\n", pop(&stack));
    printf("Top element: %d\n", peek(&stack));
    return 0;
}
//WAP to evaluate post-fix operation

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the stack structure
struct Stack {
    int top;
    unsigned capacity;
    int* array;
};

// Create a stack with the given capacity
struct Stack* createStack(unsigned capacity) {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    if (!stack)
        return NULL;
    
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    if (!stack->array)
        return NULL;

    return stack;
}

// Check if the stack is empty
int isEmpty(struct Stack* stack) {
    return stack->top == -1;
}

// Get the top element of the stack
int peek(struct Stack* stack) {
    if (!isEmpty(stack))
        return stack->array[stack->top];
    return -1; // return -1 if stack is empty
}

// Pop the top element from the stack
int pop(struct Stack* stack) {
    if (!isEmpty(stack))
        return stack->array[stack->top--];
    return -1; // return -1 if stack is empty
}

// Push an element to the stack
void push(struct Stack* stack, int op) {
    if (stack->top == (int)(stack->capacity - 1))
        return; // stack overflow
    stack->array[++stack->top] = op;
}

// Evaluate a postfix expression
int evaluatePostfix(char* exp) {
    struct Stack* stack = createStack(strlen(exp));
    if (!stack)
        return -1;

    int i;

    // Scan all characters one by one
    for (i = 0; exp[i]; ++i) {
        // If the scanned character is an operand (number), push it to the stack
        if (isdigit(exp[i])) {
            push(stack, exp[i] - '0');
        } else {
            // The scanned character is an operator, pop two elements from the stack and apply the operator
            int val1 = pop(stack);
            int val2 = pop(stack);

            switch (exp[i]) {
                case '+':
                    push(stack, val2 + val1);
                    break;
                case '-':
                    push(stack, val2 - val1);
                    break;
                case '*':
                    push(stack, val2 * val1);
                    break;
                case '/':
                    if (val1 != 0) {
                        push(stack, val2 / val1);
                    } else {
                        printf("Error: Division by zero\n");
                        free(stack->array);
                        free(stack);
                        return -1;
                    }
                    break;
            }
        }
    }

    int result = pop(stack);
    free(stack->array);
    free(stack);
    return result;
}

int main() {
    char exp[] = "231*+9-";
    printf("Postfix evaluation: %d\n", evaluatePostfix(exp));
    return 0;
}

// output
// Postfix evaluation: -4
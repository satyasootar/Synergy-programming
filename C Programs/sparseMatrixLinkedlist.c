#include <stdio.h>
#include <stdlib.h>

// Node structure for the linked list
struct Node
{
    int value;
    int row_position;
    int column_position;
    struct Node *next;
};

// Function to create a new node and append it to the end of the linked list
void create_new_node(struct Node** start, int non_zero_element,
                     int row_index, int column_index)
{
    struct Node *temp, *r;
    temp = *start;

    // Create a new node
    r = (struct Node *)malloc(sizeof(struct Node));
    if (r == NULL)
    {
        fprintf(stderr, "Memory allocation failed.\n");
        return;
    }
    
    r->value = non_zero_element;
    r->row_position = row_index;
    r->column_position = column_index;
    r->next = NULL;

    // If the linked list is empty, make the new node the start
    if (temp == NULL)
    {
        *start = r;
    }
    else
    {
        // Traverse to the end of the linked list and add the new node
        while (temp->next != NULL)
            temp = temp->next;
        
        temp->next = r;
    }
}

// Function to print the linked list representing the sparse matrix
void PrintList(struct Node *start)
{
    struct Node *temp;
    temp = start;

    printf("row_position: ");
    while (temp != NULL)
    {
        printf("%d ", temp->row_position);
        temp = temp->next;
    }
    printf("\n");

    printf("column_position: ");
    temp = start;
    while (temp != NULL)
    {
        printf("%d ", temp->column_position);
        temp = temp->next;
    }
    printf("\n");

    printf("Value: ");
    temp = start;
    while (temp != NULL)
    {
        printf("%d ", temp->value);
        temp = temp->next;
    }
    printf("\n");
}

// Main function to demonstrate the usage of the sparse matrix linked list
int main()
{
    int sparseMatrix[4][5] =
    {
        {0, 0, 3, 0, 4},
        {0, 0, 5, 7, 0},
        {0, 0, 0, 0, 0},
        {0, 2, 6, 0, 0}
    };

    struct Node* start = NULL;

    // Populate the linked list with non-zero elements from the sparseMatrix
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (sparseMatrix[i][j] != 0)
            {
                create_new_node(&start, sparseMatrix[i][j], i, j);
            }
        }
    }

    // Print the linked list
    PrintList(start);

    // Free dynamically allocated memory
    struct Node *temp;
    while (start != NULL)
    {
        temp = start;
        start = start->next;
        free(temp);
    }

    return 0;
}

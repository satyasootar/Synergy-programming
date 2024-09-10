/*WAP to implement the operations of double linked list*/


#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

// Insert a node at the beginning
void insertAtBeginning(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = *head_ref;
    new_node->prev = NULL;
    
    if (*head_ref != NULL) {
        (*head_ref)->prev = new_node;
    }
    
    *head_ref = new_node;
}

// Insert a node at the end
void insertAtEnd(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    struct Node* last = *head_ref;
    new_node->data = new_data;
    new_node->next = NULL;

    if (*head_ref == NULL) {
        new_node->prev = NULL;
        *head_ref = new_node;
        return;
    }

    while (last->next != NULL) {
        last = last->next;
    }
    
    last->next = new_node;
    new_node->prev = last;
}

// Insert a node at a specific position
void insertAtPosition(struct Node** head_ref, int new_data, int position) {
    if (position == 1) {
        insertAtBeginning(head_ref, new_data);
        return;
    }
    
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    struct Node* temp = *head_ref;

    for (int i = 1; i < position - 1 && temp != NULL; i++) {
        temp = temp->next;
    }
    
    if (temp == NULL) {
        printf("Position is out of bounds.\n");
        free(new_node);
        return;
    }
    
    new_node->next = temp->next;
    new_node->prev = temp;
    
    if (temp->next != NULL) {
        temp->next->prev = new_node;
    }
    
    temp->next = new_node;
}

// Delete a node by key
void deleteNode(struct Node** head_ref, int key) {
    struct Node* temp = *head_ref;

    while (temp != NULL && temp->data != key) {
        temp = temp->next;
    }
    
    if (temp == NULL) {
        printf("Key not found in the list.\n");
        return;
    }
    
    if (temp->prev != NULL) {
        temp->prev->next = temp->next;
    } else {
        *head_ref = temp->next;
    }
    
    if (temp->next != NULL) {
        temp->next->prev = temp->prev;
    }
    
    free(temp);
}

// Print the list in forward direction
void printListForward(struct Node* node) {
    while (node != NULL) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("NULL\n");
}

// Print the list in backward direction
void printListBackward(struct Node* node) {
    struct Node* last = NULL;

    while (node != NULL) {
        last = node;
        node = node->next;
    }

    while (last != NULL) {
        printf("%d -> ", last->data);
        last = last->prev;
    }
    printf("NULL\n");
}

int main() {
    struct Node* head = NULL;

    insertAtEnd(&head, 1);
    insertAtEnd(&head, 2);
    insertAtEnd(&head, 3);
    printListForward(head);

    insertAtBeginning(&head, 0);
    printListForward(head);  

    insertAtPosition(&head, 9, 3);
    printListForward(head);  

    deleteNode(&head, 2);
    printListForward(head);  

    printListBackward(head);  

    return 0;
}

//output
/*1 -> 2 -> 3 -> NULL
0 -> 1 -> 2 -> 3 -> NULL
0 -> 1 -> 9 -> 2 -> 3 -> NULL
0 -> 1 -> 9 -> 3 -> NULL
3 -> 9 -> 1 -> 0 -> NULL*/

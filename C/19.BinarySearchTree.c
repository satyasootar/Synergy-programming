#include <stdio.h>
#include <stdlib.h>

struct node {
  int key;
  struct node *left, *right;
};

// Create a new node
struct node *newNode(int item) {
  struct node *temp = (struct node *)malloc(sizeof(struct node));
  temp->key = item;
  temp->left = temp->right = NULL;
  return temp;
}

// In-order traversal
void inorder(struct node *root) {
  if (root != NULL) {
    inorder(root->left);
    printf("%d -> ", root->key);
    inorder(root->right);
  }
}

// Insert a node in the BST
struct node *insert(struct node *node, int key) {
  if (node == NULL) return newNode(key);

  // Traverse to the correct position and insert the new node
  if (key < node->key)
    node->left = insert(node->left, key);
  else
    node->right = insert(node->right, key);

  return node;
}

// Find the in-order successor
struct node *minValueNode(struct node *node) {
  struct node *current = node;

  // Loop down to find the leftmost leaf
  while (current && current->left != NULL)
    current = current->left;

  return current;
}

// Delete a node from the BST
struct node *deleteNode(struct node *root, int key) {
  // Return if the tree is empty
  if (root == NULL) return root;

  // Find the node to delete
  if (key < root->key)
    root->left = deleteNode(root->left, key);
  else if (key > root->key)
    root->right = deleteNode(root->right, key);
  else {
    // Node with only one child or no child
    if (root->left == NULL) {
      struct node *temp = root->right;
      free(root);
      return temp;
    } else if (root->right == NULL) {
      struct node *temp = root->left;
      free(root);
      return temp;
    }

    // Node with two children: Get the in-order successor
    struct node *temp = minValueNode(root->right);

    // Copy the in-order successor's content to this node
    root->key = temp->key;

    // Delete the in-order successor
    root->right = deleteNode(root->right, temp->key);
  }
  return root;
}

// Driver code
int main() {
  struct node *root = NULL;
  root = insert(root, 8);
  root = insert(root, 3);
  root = insert(root, 1);
  root = insert(root, 6);
  root = insert(root, 7);
  root = insert(root, 10);
  root = insert(root, 14);
  root = insert(root, 4);

  printf("Inorder traversal: ");
  inorder(root);

  printf("\nAfter deleting 10\n");
  root = deleteNode(root, 10);
  printf("Inorder traversal: ");
  inorder(root);

  return 0;
}


// OUTPUT 
// Inorder traversal: 1 -> 3 -> 4 -> 6 -> 7 -> 8 -> 10 -> 14 -> 
// After deleting 10
// Inorder traversal: 1 -> 3 -> 4 -> 6 -> 7 -> 8 -> 14 -> 
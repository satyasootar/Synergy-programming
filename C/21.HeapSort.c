//WAP to implement heap sort algorithm
#include <stdio.h>

// Function to swap two integers using pointers
void swap(int *a, int *b) {
int temp = *a;
*a = *b;
*b = temp;
}

// Function to "heapify" a subtree rooted at node i
void heapify(int arr[], int n, int i) {
int largest = i; // Initialize largest as root
int left = 2 * i + 1; // Left child index
int right = 2 * i + 2; // Right child index

// If left child is larger than root
if (left < n && arr[left] > arr[largest])
    largest = left;

// If right child is larger than the largest so far
if (right < n && arr[right] > arr[largest])
    largest = right;

// If largest is not the root
if (largest != i) {
    swap(&arr[i], &arr[largest]); // Swap root with the largest
    heapify(arr, n, largest);    // Recursively heapify the affected subtree
}

}

// Function to perform heap sort
void heapSort(int arr[], int n) {
// Build max heap
for (int i = n / 2 - 1; i >= 0; i--)
heapify(arr, n, i);

// Extract elements from the heap one by one
for (int i = n - 1; i >= 0; i--) {
    swap(&arr[0], &arr[i]);  // Move current root to end
    heapify(arr, i, 0);      // Heapify the reduced heap
}

}

// Function to print an array
void printArray(int arr[], int n) {
for (int i = 0; i < n; i++)
printf("%d ", arr[i]);
printf("\n");
}

// Main function
int main() {
int n;

// Input: Number of elements
printf("Enter the number of elements: ");
scanf("%d", &n);
int arr[n];

// Input: Elements of the array
printf("Enter the elements: \n");
for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
}

// Print original array
printf("Original array:\n");
printArray(arr, n);

// Perform heap sort
heapSort(arr, n);

// Print sorted array
printf("Sorted array:\n");
printArray(arr, n);

return 0;

}


// OUTPUT
// Enter the elements: 
// 1
// 5
// 3
// 7
// 2
// Original array:
// 1 5 3 7 2 
// Sorted array:
// 1 2 3 5 7 
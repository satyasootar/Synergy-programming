//WAP to implement quickSort algorithm

#include <stdio.h>

// Function to swap elements
void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

// Function to find the partition position
int partition(int array[], int low, int high) {
    // Select the rightmost element as pivot
    int pivot = array[high];
    int i = (low - 1); // Pointer for the greater element

    // Traverse each element of the array
    for (int j = low; j < high; j++) {
        if (array[j] <= pivot) {
            // Swap element at i with element at j
            i++;
            swap(&array[i], &array[j]);
        }
    }

    // Swap the pivot element with the greater element at i
    swap(&array[i + 1], &array[high]);
    
    // Return the partition point
    return (i + 1);
}

// QuickSort function
void quickSort(int array[], int low, int high) {
    if (low < high) {
        // Find the pivot element such that elements smaller than pivot are on left of pivot
        // Elements greater than pivot are on right of pivot
        int pi = partition(array, low, high);

        // Recursive call on the left of pivot
        quickSort(array, low, pi - 1);

        // Recursive call on the right of pivot
        quickSort(array, pi + 1, high);
    }
}

// Function to print array elements
void printArray(int array[], int size) {
    for (int i = 0; i < size; ++i) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

// Main function
int main() {
    int data[] = {8, 7, 2, 1, 0, 9, 6};
    int n = sizeof(data) / sizeof(data[0]);

    printf("Unsorted Array:\n");
    printArray(data, n);

    // Perform quicksort on data
    quickSort(data, 0, n - 1);

    printf("Sorted array in ascending order:\n");
    printArray(data, n);

    return 0;
}
//output
// Unsorted Array:
// 8 7 2 1 0 9 6 
// Sorted array in ascending order:
// 0 1 2 6 7 8 9 
#include <stdio.h>

int getMax(int a[], int n) {
    int max = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > max)
            max = a[i];
    }
    return max; // Maximum element from the array
}

void countSort(int a[], int n) {
    int output[n];
    int max = getMax(a, n);
    int count[max + 1];

    // Initialize count array with all zeros
    for (int i = 0; i <= max; ++i) {
        count[i] = 0;
    }

    // Store the count of each element
    for (int i = 0; i < n; i++) {
        count[a[i]]++;
    }

    // Find cumulative frequency
    for (int i = 1; i <= max; i++) {
        count[i] = count[i] + count[i - 1];
    }

    // Build the output array in sorted order
    for (int i = n - 1; i >= 0; i--) {
        output[--count[a[i]]] = a[i];
    }

    // Copy the sorted elements into the original array
    for (int i = 0; i < n; i++) {
        a[i] = output[i];
    }
}

void printArray(int a[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

int main() {
    int a[100], n, i;
    printf("Enter the size of an array:\n");
    scanf("%d", &n);

    printf("Enter the %d elements of array\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    printf("Before sorting array elements are - \n");
    printArray(a, n);

    countSort(a, n);

    printf("\nAfter sorting array elements are - \n");
    printArray(a, n);

    return 0;
}

// Output 
// Enter the 4 elements of array
// 2
// 1
// 65
// 32
// Before sorting array elements are - 
// 2 1 65 32 
// After sorting array elements are - 
// 1 2 32 65
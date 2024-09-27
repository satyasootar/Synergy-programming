#include <stdio.h>

/* Function to merge the subarrays of a[] */
void merge(int a[], int beg, int mid, int end) {
    int n1 = mid - beg + 1;
    int n2 = end - mid;

    int LeftArray[n1], RightArray[n2]; // temporary arrays

    /* Copy data to temp arrays */
    for (int i = 0; i < n1; i++)
        LeftArray[i] = a[beg + i];
    for (int j = 0; j < n2; j++)
        RightArray[j] = a[mid + 1 + j];

    int i = 0, j = 0, k = beg;  // Initial indices of the two subarrays and the merged array

    /* Merge the temp arrays back into a[] */
    while (i < n1 && j < n2) {
        if (LeftArray[i] <= RightArray[j]) {
            a[k] = LeftArray[i];
            i++;
        } else {
            a[k] = RightArray[j];
            j++;
        }
        k++;
    }

    /* Copy the remaining elements of LeftArray[], if any */
    while (i < n1) {
        a[k] = LeftArray[i];
        i++;
        k++;
    }

    /* Copy the remaining elements of RightArray[], if any */
    while (j < n2) {
        a[k] = RightArray[j];
        j++;
        k++;
    }
}

/* Function to sort the array using merge sort */
void mergeSort(int a[], int beg, int end) {
    if (beg < end) {
        int mid = beg + (end - beg) / 2;  // Find the middle point

        mergeSort(a, beg, mid);  // Sort first half
        mergeSort(a, mid + 1, end);  // Sort second half
        merge(a, beg, mid, end);  // Merge the sorted halves
    }
}

/* Function to print the array */
void printArray(int a[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main() {
    int a[] = {12, 31, 25, 8, 32, 17, 40, 42};
    int n = sizeof(a) / sizeof(a[0]);

    printf("Before sorting, array elements are - \n");
    printArray(a, n);

    mergeSort(a, 0, n - 1);

    printf("After sorting, array elements are - \n");
    printArray(a, n);

    return 0;
}

// output 
// Before sorting, array elements are - 
// 12 31 25 8 32 17 40 42 
// After sorting, array elements are - 
// 8 12 17 25 31 32 40 42 
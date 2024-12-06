#include <stdio.h>

int main() {
    int arr[100], i, key, n;
    int low, high, mid;

    printf("Enter the number of values you want to declare: ");
    scanf("%d", &n);

    printf("Enter %d values in ascending/descending order:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the number you want to search: ");
    scanf("%d", &key);

    low = 0;
    high = n - 1;

    while (low <= high) {
        mid = (low + high) / 2;

        if (arr[mid] < key) {
            low = mid + 1;
        } else if (arr[mid] > key) {
            high = mid - 1;
        } else { 
            printf("Found the value at position %d\n", mid+1);
            return 0; 
        }
    }

    printf("Value %d not found in the array.\n", key);
    return 0;
}


// OUTPUT
// Enter the number of values you want to declare: 5
// Enter 5 values in ascending/descending order:
// 1 2 3 4 5
// Enter the number you want to search: 4
// Found the value at position 4
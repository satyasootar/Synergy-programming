//Date - 1/3/25

//Question-
//Sort a given set of n integer elements using Quick Sort method and compute its time complexity. Run the program for varied values of n> 5000 and record the time taken to sort. Plot a graph of the time taken versus n. The elements can be read from a file or can be generated using the random number generator. Demonstrate how the divide-and- conquer method works along with its time complexity analysis: worst case, average case and best case.


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int arr[], int i, int j)
{
int temp = arr[i];
arr[i] = arr[j];
arr[j] = temp;
}

int partition(int arr[], int low, int high)
{
int pivot = arr[high];
int i = low - 1;

for (int j = low; j < high; j++) 
{
    if (arr[j] < pivot) 
    {
        i++;
        swap(arr, i, j);
    }
}
swap(arr, i + 1, high);
return (i + 1);
}

// Quick Sort function
void quickSort(int arr[], int low, int high)
{
if (low < high)
{
int pi = partition(arr, low, high);

    quickSort(arr, low, pi - 1);  // Before pivot
    quickSort(arr, pi + 1, high); // After pivot
}
}

int main()
{
int n;
srand(time(NULL));

printf("Enter the size of the array: ");
scanf("%d", &n);
int arr[n];
for (int i = 0; i < n; i++) 
{
    arr[i] = rand() % 100000; // Random numbers between 0 and 99999
}

clock_t start_time = clock();
quickSort(arr, 0, n - 1);
clock_t end_time = clock();

double time_taken = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
printf("Time taken to sort the array: %f seconds\n", time_taken);
printf("Sorted Array:(First 10 elements\n");
for (int i = 0; i < 10; i++) 
{
     printf("%d ", arr[i]);
}
printf("\n");

return 0;
}


//output
// Enter the size of the array: 25000
// Time taken to sort the array: 0.004167 seconds
// Sorted Array:(First 10 elements
// 0 6 12 15 21 24 25 27 33 43


// Time complexity
// Worst case: O(n^2)
// Avg case: O(n log n)
// Best case: O(n log n)
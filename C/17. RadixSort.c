#include <stdio.h>  

int getMax(int a[], int n) {  
   int max = a[0];  
   for(int i = 1; i < n; i++) {  
      if(a[i] > max)  
         max = a[i];  
   }  
   return max;  
}  

void countingSort(int a[], int n, int place) {  
  int output[n + 1];  
  int count[10] = {0};    
  
  for (int i = 0; i < n; i++)  
    count[(a[i] / place) % 10]++;  
  
  for (int i = 1; i < 10; i++)  
    count[i] += count[i - 1];  
  
  for (int i = n - 1; i >= 0; i--) {  
    output[count[(a[i] / place) % 10] - 1] = a[i];  
    count[(a[i] / place) % 10]--;  
  }  
  
  for (int i = 0; i < n; i++)  
    a[i] = output[i];  
}  

void radixsort(int a[], int n) {  
  int max = getMax(a, n);  
  
  for (int place = 1; max / place > 0; place *= 10)  
    countingSort(a, n, place);  
}  

void printArray(int a[], int n) {  
  for (int i = 0; i < n; ++i) {  
    printf("%d  ", a[i]);  
  }  
  printf("\n");  
}  

int main() {  
  int a[100], n, i;
  
  printf("Enter the size of an array:\n");
  scanf("%d", &n);
  
  printf("Enter the %d elements of the array:\n", n);
  for (i = 0; i < n; i++)  
    scanf("%d", &a[i]); 
  
  printf("Before sorting, the array elements are:\n");
  printArray(a, n);  
  
  radixsort(a, n);   
  
  printf("\nAfter sorting, the array elements are:\n");    
  printArray(a, n);  
  
  return 0;
}

// Output 
// Enter the size of an array:
// 5
// Enter the 5 elements of the array:
// 321
// 455
// 654 
// 342
// 434     
// Before sorting, the array elements are:
// 321  455  654  342  434  

// After sorting, the array elements are:
// 321  342  434  455  654 
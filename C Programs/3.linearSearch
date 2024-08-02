#include <stdio.h>

int main() {
    int arr[100], i, key, n , value, count = 0;
   
    printf("Enter the number of values you want to declare: ");
    scanf("%d", &n);

    printf("Enter %d values in ascending/descending order:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    printf("Enter the number you want to search: ");
    scanf("%d", &key);
       
    for(i = 0; i< n; i++){
        if(arr[i] == key){
            count++;
            value = i+1;
        }
    }   
            if(count == 1){
            printf("found the value at pos %d", value );
        }else{
            printf("Invalid input" );
        }
}

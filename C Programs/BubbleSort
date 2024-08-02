#include<stdio.h>
int main()
{
    int arr[100],n,i,j,temp;
    printf("Enter the number of elements you want to take as an input:\n");
    scanf("%d",&n);
    printf("Enter %d numbers\n",n);
    for(i=0;i<n;i++)
     {
         printf("Element %d=",i+1);
         scanf("%d",&arr[i]);
     }
    printf("Before Sorting the array elements are:\n");
    for(i=0;i<n;i++)
     {
         printf("%d ",arr[i]);
     }
     
//Bubble Sort logic starts here
    for(i=0;i<n-1;i++) //Outer loop for passes
     {
         int flag=0;  //For optimized bubble sort
         for(j=0;j<n-1-i;j++)  //Inner loop for comparisons
          {
              if(arr[j]>arr[j+1])
               {
                 //Swap the two adjacent numbers
                   temp=arr[j];
                   arr[j]=arr[j+1];
                   arr[j+1]=temp;
                   flag=1;
               }
          }
          if(flag==0)
            break;
           
     }
     printf("\nAfter Sorting the elements are:\n");
     for(i=0;i<n;i++)
      {
          printf("%d ",arr[i]);
      }
     return 0;
}


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
         printf("%d  ",arr[i]);
     }
     

   for(i=1;i<n;i++) //For unsorted list
     {
         temp=arr[i]; //tem variable
         j=i-1;
         while(j>=0 && arr[j]>temp) //For Comparisons
          {
              arr[j+1]=arr[j];
              j--; //sorted list
          }
         arr[j+1]=temp; //sorted list
       
    }
    
    printf("\nAfter Sorting the elements are:\n");
     for(i=0;i<n;i++)
      {
          printf("%d ",arr[i]);
      }
     return 0;
}
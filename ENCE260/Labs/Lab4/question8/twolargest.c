#include <stdio.h>
#include <stdlib.h>

int compare(const void* val1, const void* val2) 
{
    return ( *(int*)val1 - *(int*)val2 );
}

void rvereseArray(int arr[], int start, int end) 
{ 
    int temp; 
    while (start < end) { 
        temp = arr[start];    
        arr[start] = arr[end]; 
        arr[end] = temp; 
        start++; 
        end--; 
    }    
}

void findTwoLargest(int data[], int n, int* largest, int* secondLargest)
{ 
    int reversible[n];
    for (int i = 0; i < n; i++) {
        reversible[i] = data[i];
    }
    qsort(reversible, n, sizeof(int), compare);
    rvereseArray(reversible, 0, n-1);
    *largest = reversible[0];
    *secondLargest = reversible[1];
}

int main(void)
{
int data[] = {4, 5};
int result1 = 0, result2 = 0;
findTwoLargest(data, 2, &result1, &result2);
printf("%d %d\n", result1, result2);
printf("%d %d\n", data[0], data[1]);
}

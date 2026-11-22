#include <stdio.h>

// I'll write a function to find the smallest element in an array
int find_smallest(int array[], int size) {

    // Stores the smallest value
    int smallest = array[0];

    // Stores the index of the smallest value
    int smallest_index = 0;

    // We already have the 0-th index, so we are now starting from 1-th index
    for(int i = 1; i < size; i++) {
        if (array[i] < smallest) {
            smallest = array[i];
            smallest_index = i;
        }
    }

    return smallest_index;
}

int selection_sort(int array[], int size, int newArray[]) {
    int copiedArray[size];
    int copiedArrayLength = size; // Track the shrinking size for our simulated pop
    
    // Copy the original array
    for(int i = 0; i < size; i++) {
        copiedArray[i] = array[i];
    }

    for(int i = 0; i < size; i++) {

        // Find the smallest in the remaining copied array...
        int smallest = find_smallest(copiedArray, copiedArrayLength);
        
        newArray[i] = copiedArray[smallest];
        
        // Manually pop the array and shift the element
        for (int j = smallest; j < copiedArrayLength -1; j++) {
            copiedArray[j] = copiedArray[j + 1];
        }
        copiedArrayLength--;    // Shrink the active tracker
    }
}

int main(void) {
    int my_array[] = {5, 3, 6, 2, 10};
    int size = 5;
    int newArray[size];

    selection_sort(my_array, size, newArray);

    // Now the array is sorted. Let's print it.
    printf("Sorted array: [");
    for (int i = 0; i < size; i++) {
        printf("%d", newArray[i]);
        if(i < size - 1) {
            printf(", ");
        }
    }
    printf("]\n");

    return 0;
}
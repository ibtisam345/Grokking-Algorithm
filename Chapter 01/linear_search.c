#include <stdio.h>

int linear_search(int array[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (array[i] == target) {
            return i;
        }
    }

    return -1;
}

int main(void) {
    int my_array[] = {4, 5, 1, 9, 8, 7, 10};
    int size = 7;
    int target = 8;

    int result = linear_search(my_array, size, target);

    if (result != -1) {
        printf("Found %d at index %d\n", target, result);
    }
    else {
        printf("%d not found in the array!\n", target);
    }

    return 0;
}
#include <stdio.h>

int binary_search(int array[], int n, int target) {

    // low and high keep track of which part of the list I'll search in
    int low = 0;
    int high = n - 1;

    // While I haven't narrowed it down to one element...
    while (low <= high) {
        int mid = (low + high) / 2;
        int guess = array[mid];

        // Found the target
        if (guess == target) {
            return mid;
        }

        // The guess was too low
        else if (guess < target) {
            low = mid + 1;
        }

        // The guess was too high
        else {
            high = mid - 1;
        }
        
    }

    // The target doesn't exist
    return -1;
}

int main(void) {
    int my_list[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = 10;

    printf("%d\n", binary_search(my_list, n, 3));           // 2
    printf("%d\n", binary_search(my_list, n, -1));          // -1

    return 0;
}
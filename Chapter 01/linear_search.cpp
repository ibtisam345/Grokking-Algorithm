#include <iostream>

int linear_search(int array[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (array[i] == target) {
            return i;
        }
    }

    return -1;
}

int main() {
    int array[] = {4, 5, 1, 9, 8, 7, 10};
    int size = 7;
    int target = 8;

    int result = linear_search(array, size, target);

    if (result != -1) {
        std::cout << "Found " << target << " at index " << result << "!";
    }
    else {
        std::cout << target << " not found in the array!";
    }

    return 0;
}
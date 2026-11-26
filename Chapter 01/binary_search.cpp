#include <iostream>

int binary_search(int array[], int size, int target) {
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (array[mid] == target) {
            return mid;
        }
        else if (array[mid] > target) {
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }

    return -1;
}
int main() {
    int my_array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = 10;
    
    std::cout << binary_search(my_array, size, 8) << '\n';      // 7
    std::cout << binary_search(my_array, size, 2) << '\n';      // 1
    std::cout << binary_search(my_array, size, -1) << '\n';     // -1

    return 0;
}
def binary_search(array, target):

    # low and high keep track of which part of the list I'll search in
    low = 0
    high = len(array) - 1

    # While I haven't narrowed it down to one element...
    while low <= high:

        # // is the floor division. 
        # same as: mid = int((low + high) / 2)
        mid = (low + high) // 2     # Check the middle element
        guess = array[mid]

        if guess == target:         # Found the target
            return mid              
        elif guess < target:        # The guess was too low
            low = mid + 1
        else:                       # The guess was too high
            high = mid - 1
    return None                     # The target doesn't exist

def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(binary_search(my_list, 2))        # prints 1
    print(binary_search(my_list, -18))      # prints None

if __name__ == "__main__":
    main()
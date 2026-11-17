def quickSort(array):

    # Let's define the base case
    # for an array having 0 or 1 element
    # Because, an array with 0 or 1 elements is already sorted.
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        # less = [i for i in array[1:] if i<= pivot]
        # greater = [i for i in array[1:] if i > pivot]

        less = []
        greater = []
        for i in array[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
        # The recursive case
        return quickSort(less) + [pivot] + quickSort(greater)

def main():
    print(quickSort([9, 2, 5, 1, 7, 10, 4]))

if __name__ == "__main__":
    main()
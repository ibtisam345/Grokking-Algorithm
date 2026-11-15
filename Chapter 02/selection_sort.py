# I'll write a function to find the smallest element in an array

def findSmallest(array):

    # Stores the smallest value
    smallest = array[0]
    # Stores the index of the smallest value
    smalles_index = 0

    # We already have the 0-th index, so we now starting from 1-th index
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smalles_index = i

    return smalles_index

# Now I can use this function to write selection sort ...

def selectionSort(array):           # Sorts an array
    newArray = []                   
    copiedArray = list(array)       # Copy array elements before mutating
    for i in range(len(copiedArray)):

        # Find the smallest element in the array and adds it to the new array
        smallest = findSmallest(copiedArray)
        newArray.append(copiedArray.pop(smallest))

    return newArray

print(selectionSort([5, 3, 6, 2, 10]))
# prints [2, 3, 5, 6, 10]

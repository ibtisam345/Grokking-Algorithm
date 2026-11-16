# Question:
# Write a recursive function to find the maximum number in a list

# Took help from Google Gemini AI

def findMax(array):

    # Base case: 
    # If the list has only one item, that is maximum
    if len(array) == 1:
        return array[0]

    # If the list is empty, No max
    elif len(array) == 0:
        return None

    # find the max of the rest of the list
    sub_max = findMax(array[1:])       # <-- Recursive case

    # Compare the first element with the max of the rest
    if array[0] > sub_max:
        return array[0]
    else:
        return sub_max

def main():
    my_array = [10, 34, 89, 11, 90, 15]

    print(findMax(my_array))

main()
# Question:
# Write a recursive function to count the number of items in a list

# Okay, we will be using recursion, so we need to find a base case 
# and a recursive case

def count(arr):

    if len(arr) == 0:       # <---- the base case
        return 0

    return 1 + count(arr[1:])       # <<---- Recursive case

def main():

    my_list = [23, 9, 19, 23, 19,11, 3]
    print(count(my_list))

main()

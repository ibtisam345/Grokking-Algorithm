def linearSearch(array, target):
    for i in range(len(array)):
        guess = array[i]
        if guess == target:
            return i
    return None

def main():
    my_array = [1, 2, 3, 5, 6, 7, 10]

    print(linearSearch(my_array, 7))        # prints 5
    print(linearSearch(my_array, 8))        # prints None

if __name__ == "__main__":
    main()
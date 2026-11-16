def sum(array): 
    if array == []:                         # <<<--- The Base Case
        return 0

    return array[0] + sum(array[1:])        # <---- Recursive case

def main():
    my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(sum(my_arr))

main()

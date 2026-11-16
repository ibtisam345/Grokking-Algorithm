# Factorial is a great example of recursion

def factorial(n):
    if n == 1:          # <----- Base Case
        return 1

    return n * factorial(n - 1) # <------ Recursion!!

def main():
    
    num = int(input("Enter n: "))
    print(factorial(num))

if __name__ == "__main__":
    main()
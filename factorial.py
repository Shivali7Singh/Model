def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def main():
    while True:
        try:
            n = int(input("Enter a positive integer n: "))
            if n >= 1:
                break
            else:
                print("Please enter n ≥ 1.")
        except ValueError:
            print("Invalid input. Enter an integer.")

    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")

if __name__ == "__main__":
    main()
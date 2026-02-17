def pyramid_of_consecutive_numbers():
    rows = int(input("Enter number of rows: "))
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end='')
            num += 1
        print()  

pyramid_of_consecutive_numbers()
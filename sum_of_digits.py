
def sum_of_digits(n):
    n = abs(n) 
    total = 0
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(str(digit))
        total += digit
        n //= 10
    expression = ' + '.join(digits[::-1])
    return total, expression


num = int(input("Enter a number: "))
digit_sum, expr = sum_of_digits(num)
print(f"You entered: {num}")
print(f"Sum of digits: {expr} = {digit_sum}")
def get_sum_even_numbers(num):
    sum = 0

    while num > 0:
        digit = num % 10

        if digit % 2 == 0:
            sum += digit
        num = num // 10

    return sum

def get_sum_odd_numbers(num):
    sum = 0

    while num > 0:
        digit = num % 10

        if digit % 2 != 0:
            sum += digit
        num = num // 10

    return sum

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    evenSum = get_sum_even_numbers(num)
    oddSum = get_sum_odd_numbers(num)
    print(f"{oddSum} {evenSum}")

def get_numbers_sum(num):
    even_sum = 0
    odd_sum = 0

    for i in num:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    
    return [odd_sum,even_sum]

if __name__ == "__main__":
    num = input("Enter a number: ")
    result = get_numbers_sum(num)
    print(f"{result[0]} {result[1]}")

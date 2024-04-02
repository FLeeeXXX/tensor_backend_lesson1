import random
def get_random_number(start_number, end_number):
    return random.randint(start_number, end_number)

if __name__ == "__main__":
    user_number = (int(input("Enter a number: ")))
    guess_number = get_random_number(1, 100)

    while True:
        print(f"Вы загадали: {guess_number}?")
        userResponse = input().lower()
        if userResponse == "больше":
            if guess_number == user_number:
                print("Аферист пойман")
                break
            else:
                guess_number = get_random_number(guess_number + 1, 100)
        elif userResponse == "меньше":
            if guess_number == user_number:
                print("Аферист пойман")
                break
            else:
                guess_number = get_random_number(1, guess_number - 1)
        else:
            break
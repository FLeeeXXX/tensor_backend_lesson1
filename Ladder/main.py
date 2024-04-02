def get_ladder(size):
    for i in range(1, size + 1):
        print(' ' * (size - i) + '#' * i)

if __name__ == "__main__":
    get_ladder(int(input("Enter a number: ")))
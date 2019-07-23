def circle_of_numbers(n, firstNumber):
    return (firstNumber + (n / 2)) % n


if __name__ == "__main__":
    n = input("Enter 'n': ")
    while not n.isdigit():
        n = input("Please enter a valid number 'n': ")
    firstNumber = input("Enter 'firstNumber': ")
    while not firstNumber.isdigit():
        firstNumber = input("Please enter a valid number 'firstNumber': ")
    res = circle_of_numbers(int(n), int(firstNumber))
    print(res)

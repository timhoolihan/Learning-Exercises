import math

while True:
    number = input("Enter a number to check if it's prime: ")
    try:
        number = int(number)
        root = math.sqrt(number)
        if root % 1 == 0:
            print(f"Yes, {number} is a prime number. The square root is {root}.")
        else:
            print(f"No, {number} is not a prime number.")
    except:
        print("Invalid input. Try again")
import random

answer = random.randrange(1, 100)
count = 0

print("Guess if the number is higher or lower")

while True:
    number = input("Guess a number: ")
    try:
        number = int(number)
        if number < answer:
            print("Number is higher. ")
            count = count + 1
        if number > answer:
            print("Number is lower.")
            count = count + 1
        if number == answer:
            print(f"You got it in {count} tries!")        
    except ValueError:
        print("Invalid input. Try again.")
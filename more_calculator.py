numbers = []
num = ""
operator = ""
answer = 0

while True:
    if num == "=" or operator == "=":
        break
    num = input("Enter a number (or '=' to finish): ")
    try:
        match operator:
            case "":
                answer = float(num)
            case "+":
                answer += float(num)
            case "-":
                answer -= float(num)
            case "*" | "x":
                answer *= float(num)
            case "/,":
                if num == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    answer /= float(num)
    except ValueError:
        print("Invalid input. Please enter a valid number or '='.")
        continue

    while True:
            operator = input("Enter operator (+, -, *, /)(or '=' to finish): ")
            if operator == "=":
                break
            elif operator in ("+", "-", "*", "/", "x"):
                break
            else:
                print("Invalid operator. Please enter one of +, -, *, /.")

print(f"The answer is: {answer}")
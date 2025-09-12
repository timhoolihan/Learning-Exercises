def number_input(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except:
            print("Try again")

num1 = number_input("Enter first number: ")

while True:
    operator = input("Enter operator: ")
    if operator in ("+" "-", "/", "*", "x"):
        break
    else:
        print("Try again")
        
num2 = number_input("Enter second number: ")   

match operator:
    case "+":
        answer = (float(num1) + float(num2))
    case "-":
        answer = (float(num1) - float(num2))
    case "/":
        if float(num2) == 0:
            print("Error: Division by zero is not allowed.")
        else:
            answer = (float(num1) / float(num2))
    case "*" | "x":
        answer = (float(num1) * float(num2))
        operator = "x"

print(f"{num1} {operator} {num2}" + " is " + f"{answer}")  
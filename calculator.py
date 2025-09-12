check=True
while check==True:
    num1=input("Enter first number: ")
    try:
        float(num1)
        check=False
    except:
        print("Try again")

check=True
while check==True:
    operator=input("Enter operator: ")
    if operator in ("+", "-", "/", "*"):
        check=False
    else:
        print("Try again")
        
check=True
while check==True:
    num2=input("Enter second number: ")
    try: 
        float(num2)
        check=False
    except:
        print("Try again")
        
match operator:
    case "+":
        print(float(num1)+float(num2))
    case "-":
        print(float(num1)-float(num2))
    case "/":
        print(float(num1)/float(num2))
    case "*":
        print(float(num1)*float(num2))
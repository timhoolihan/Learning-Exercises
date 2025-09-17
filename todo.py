list = ["Test", "Maybe", "Apple"]
task = ""

print("Welcome to the to-do list. Enter a command: ")
print("Add | View")

while True:
    action = input("What would you lke to do? ")
    while action in ("Add", "View", "Remove"):
        match action:

            case "Add": #Add a task
                task = input("Enter a task: ")
                list.append(task)
                print ("Task added")
                break

            case "View": #View tasks
                x = 0
                while x < len(list):
                    entry = (list[x])
                    print(f"{x}. {entry}")
                    x = x + 1
                break

            case "Remove": #Remove tasks
                remove = input("Enter a task number to remove, or 'Back': ")
                if remove in "Back":
                    break
                elif not remove.isdigit():
                    print("Please enter a valid number.")
                    continue
                remove = int(remove)
                if remove < len(list):
                    list.pop(remove)
                    print("Task removed")
                    break             
                
    else:
        print("Invalid input. Please enter 'Add', 'View', or 'Remove'.")
        continue
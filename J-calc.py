## J-CALC GOOD TO GO!!! ##
def calc():

    print("Welcome to J-calc")
    num_3 = float(input("Please enter your first number: "))
    action = input("Please enter an operator: ")
    num_4 = float(input("Please enter your second number: "))

    if action == "+" or action.lower() == "add":
        print(num_3 + num_4)
    
    elif action == "-" or action.lower() == "subtract":
        print(num_3 - num_4)
    
    elif action == "/" or action.lower() == "divide":
        print(num_3 / num_4)

    elif action == "*" or action.lower() == "multiply":
        print(num_3 * num_4)

    elif action.lower() == "power" or action == "**":
        print(num_3 ** num_4)
    
    else:
        print("Please enter a proper math operation!")

    user = input("Restart? Y/N ")
    if user.lower() == "y" or user.lower() == "yes":
        calc()
    else:
        print("Thank you for using J-calc")
        exit()

calc()

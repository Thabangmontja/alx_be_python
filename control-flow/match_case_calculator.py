#Prompting the user for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

#Prompt the user for the type of operation.
operation = input("Choose the operation (+, -, *, /): ")

#Perform the calculation using match-case
match operation:
    case "+":
        result = number1 + number2
        print(f"The result is {result}")
    case "-":
        result = number1 - number2
        print(f"The result is {result}")
    case "*":
        result = number1 * number2
        print(f"The result is {result}")
    case "/":
        if number2 !=0:
            result = number1 / number2
            print(f"The result is {result}")
        else:
            print("cannot divide by zero")
    case _:
        print("Invalid operation. Please choose one of the following: +, -, *, /")
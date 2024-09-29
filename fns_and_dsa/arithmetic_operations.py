
# from arithmetic_operations import perform_operation

# def main():
#     print("Arithmetic Operations")
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

#     result = perform_operation(num1, num2, operation)
#     print(f"Result: {result}")

# if __name__ == "__main__":
#     main()

# def perform_operation(num1, num2, operation):
#     if operation == 'add':
#         return num1 + num2
#     elif operation == 'subtract':
#         return num1 - num2
#     elif operation == 'multiply':
#         return num1 * num2
#     elif operation == 'divide':
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Cannot divide by zero"
#     else:
#         return "Invalid operation"

def perform_operation(num1, num2, operation):
    """
    Performs the specified arithmetic operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform (add, subtract, multiply, divide).

    Returns:
        float or str: The result of the operation or an error message.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"
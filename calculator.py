# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Creating the operations dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Asking for input
def calculator():
    num1 = float(input("Enter the first number?"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Choose the operations from above ")
        num2 = float(input("Enter the next number?"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("press 'y' to continue or press 'n' to reset a calculator: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
def Calculate(num1, num2, op):

    if op == '+':
        return num1 + num2

    if op == '-':
        return num1 - num2

    if op == '*':
        return num1 * num2

    if op == '/':
        return num1 / num2 if num2 != 0 else "Error: division by zero"

    return "Incorrect operator"

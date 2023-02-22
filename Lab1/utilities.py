def number_entering(string):
    while True:  # Until number is entered
        try:
            x = int(input(string))
            break
        except ValueError:
            print("Error : invalid number")

    return x


def calculate(num1, num2, op):

    if op == '+':
        return num1 + num2

    if op == '-':
        return num1 - num2

    if op == '*':
        return num1 * num2

    if op == '/':
        return num1 / num2 if num2 != 0 else "Error: division by zero"

    return "Incorrect operator"


def get_even_nums_list(lst):
    return list(item for item in lst if item % 2 == 0)

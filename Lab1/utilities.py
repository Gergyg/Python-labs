import constants


def number_entering(string):
    while True:  # Until number is entered
        try:
            x = int(input(string))
            break
        except ValueError:
            print("Error : invalid number")

    return x


def check_operator(string):
    return True if string in constants.CORRECT_OPS else False


def operator_entering(string):
    while True:  # Until operator is correct
        operator = input(string)
        if check_operator(operator):
            break
        else:
            print(constants.INCORRECT_OP)

    return operator


def calculate(num1, num2, op):
    if not check_operator(op):
        return constants.INCORRECT_OP

    if op == '+':
        return num1 + num2

    if op == '-':
        return num1 - num2

    if op == '*':
        return num1 * num2

    if op == '/':
        return num1 / num2 if num2 != 0 else constants.ERROR_DIV_BY_ZERO


def get_even_nums_list(lst):
    return list(item for item in lst if item % 2 == 0)

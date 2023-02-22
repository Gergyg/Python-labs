import utilities


print("Hello world")

while True:
    try:
        first = int(input("Input first number: "))
        second = int(input("Input second number: "))
        break
    except ValueError:
        print("Error: invalid number")

while True:
    operator = input("Input operator(+, -, *, /): ")
    result = utilities.Calculate(first, second, operator)
    print("Result:", result)
    if result != "Incorrect operator":
        break

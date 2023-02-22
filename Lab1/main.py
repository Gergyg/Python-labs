import utilities


print("Hello world")

first = utilities.number_entering("Input first number : ")
second = utilities.number_entering("Input second number : ")

while True:  # Until operator is correct
    operator = input("Input operator(+, -, *, /) : ")
    result = utilities.calculate(first, second, operator)
    print("Result:", result)
    if result != "Incorrect operator":  # Checking if entered operator is invalid
        break


lst = []
n = utilities.number_entering("Input the number of elements in list : ")

for i in range(0, n):
    ele = utilities.number_entering("Enter element #" + str(i+1) + " : ")
    lst.append(ele)

resLst = utilities.get_even_nums_list(lst)
print("List without odd numbers : ", resLst)

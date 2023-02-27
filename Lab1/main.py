import utilities


if __name__ == "__main__":

    print("Hello world")

    first = utilities.number_entering("Input first number : ")
    second = utilities.number_entering("Input second number : ")
    operator = utilities.operator_entering("Input operator(+, -, *, /) : ")

    result = utilities.calculate(first, second, operator)
    print("Result:", result)

    lst = []
    n = utilities.number_entering("Input the number of elements in list : ")

    for i in range(0, n):
        ele = utilities.number_entering("Enter element #" + str(i+1) + " : ")
        lst.append(ele)

    resLst = utilities.get_even_nums_list(lst)
    print("List without odd numbers : ", resLst)

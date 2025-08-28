def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

print("Welcome to the calculator, the place where you calculate")

def main():
    cont = True
    num1 = float(input("Give me your first number: "))
    while cont:
        operation = input("+\n-\n*\n/\nWhich operation: ")
        num2 = float(input("Give me your second number: "))

        new_num = operations[operation](n1=num1,n2=num2)
        print(new_num)

        status = input("If you want to continue working on this result, type 'c'\nIf you want to start a new equation, type 'n'\nIf you want to quit, type 'q': ")
        if status == "n":
            cont = False
            print("\n"*100)
        elif status == "c":
            num1 = new_num
        else:
            return
    main()
main()

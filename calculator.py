# menu
# 1 add 2 numbers
# 2 subtract 2 numbers
# 3 multiply 2 numbers
# 4 divide 2 numbers
# quit

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def print_menu():
    print("1 add 2 numbers\n2 subtract 2 numbers\n3 multiply 2 numbers\n4 divide 2 numbers\n5 quit: ")

def get_inputs(option):
    while True:
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        if x.isdigit() and y.isdigit() and (int(option) <= 4 and int(y) != 0):
            return int(x), int(y)

def get_menu_selection():
    while True:
        n = input("Enter a selection 1 - 5\n")
        if n.isdigit() and 1 <= int(n) <= 5:
            return int(n)

print_menu()
while True:
    option = get_menu_selection()
    if option == 5:
        break
    x, y = get_inputs(option)
    if option == 1:
        print(add(x, y))
    elif option == 2:
        print(subtract(x, y))
    elif option == 3:
        print(multiply(x, y))
    elif option == 4:
        print(divide(x, y))

    
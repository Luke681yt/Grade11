def print_menu():
    print("1-add AB and CD\n2-subtract AB and CD\n3-multiply AB and CD\n4-divide AB and CD\n5-inversing\n6-exponentiating")


def menu_selection():
    while True:
        try:
            n = input("enter menu selection:\n")
            if int(n) > 0 and int(n) < 7:
                return int(n)
        except:
            print("enter a valid input\n")

#line 1-13 is making the menu printing function and making a way to get the menu selection from the user and validating it

def mixed_to_improper(f: str):
    try:
        space = f.find(" ")
        slash = f.find("/")
        px = f[:space]
        p1 = f[space+1:slash]
        p2 = f[slash+1:]
        p1 = int(p1)
        p2 = int(p2)
        px = int(px)
        p1 = ((p2*px)+p1)
        return p1, p2
    except:
        try:
            slash = f.find("/")
            p1 = f[:slash]
            p2 = f[slash+1:]
            p1 = int(p1)
            p2 = int(p2)
            return p1, p2
        except:
            print("invalid input")

#line 16-37 sets up the mixed to improper function

def improper_to_mixed(p1: int, p2: int):
    if p1 < 0 and p2 < 0:
        p1 = abs(p1)
        p2 = abs(p2)
        if p1 % p2 == 0:
            x = p1/p2
            return (f"{x}")
        elif p1 > p2 and p1 % p2 != 0:
            mx = p1//p2
            p1 = p1-(p2*mx)
            return (f"{mx} {p1}/{p2}")
        elif p1 < p2:
            return (f"{p1}/{p2}")
        else:
            print("error")
    elif p1 > 0 and p2 > 0:
        if p1 % p2 == 0:
            x = p1/p2
            return (f"{x}")
        elif p1 > p2 and p1 % p2 != 0:
            mx = p1//p2
            p1 = p1-(p2*mx)
            return (f"{mx} {p1}/{p2}")
        elif p1 < p2:
            return (f"{p1}/{p2}")
        else:
            print("error")
    elif p1 < 0 or p2 < 0:
        p2, p1 = abs(p2), abs(p1)
        if p1 % p2 == 0:
            mx = p1/p2
            mx = mx*(-1)
            return (f"{mx}")
        elif p1 > p2 and p1 % p2 != 0:
            mx = p1//p2
            p1 = p1-(p2*mx)
            mx = mx*(-1)
            return (f"{mx} {p1}/{p2}")
        elif p1 < p2:
            p1 = p1*-1
            return (f"{p1}/{p2}")
#line 41-83 is my improper to mixed function; I also included formatting in this function because it's far easier than making a seperate function for formatting

def simplify(p1: int, p2: int):
    for i in range(p2, 0, -1):
        if p1 % i == 0 and p2 % i == 0:
            p1 = p1/i
            p2 = p2/i
            return p1, p2
    return p1, p2

#line 83-90 is simplification

def get_input():
    while True:
        x = str(input("input fraction A\n"))
        y = str(input("input fraction B\n"))
        try:
            x1, x2 = mixed_to_improper(x)
            y1, y2 = mixed_to_improper(y)
            return (x1, x2, y1, y2)
        except:
            print("please enter a valid input")

#line 94-103 gets the user input (fractions) and validates the input


def add_frac(x1: int, x2: int, y1: int, y2: int):
    if x2 == y2:
        p1 = x1+y1
        p2 = x2
        return p1, p2
    elif x2 != y2:
        p2 = x2*y2
        p1 = (x1*y2)+(y1*x2)
        return p1, p2
#line 108-116 is my add fraction function

def sub_frac(x1: int, x2: int, y1: int, y2: int):

    if x2 == y2:
        p1 = x1-y1
        p2 = x2
        return p1, p2
    elif x2 != y2:
        p2 = x2*y2
        p1 = (x1*y2)-(y1*y2)
        return p1, p2
#line 119-128 is my subtraction function

def multiply_frac(x1: int, x2: int, y1: int, y2: int):
    p1 = x1*y1
    p2 = x2*y2
    return p1, p2

#line 131-134 is my multiply fraction function

def divide_frac(x1: int, x2: int, y1: int, y2: int):
    p1 = x1*y2
    p2 = x2*y1
    return p1, p2

#line 138-141 is my divide fraction function

def inversing():
    while True:
        try:
            x = input("input fraction A\n")
            x1, x2 = mixed_to_improper(x)
            x1, x2 = simplify(x1, x2)
            x = improper_to_mixed(x2, x1)
            return (x)
        except:
            print("invalid input")
#line 145 is my fraction inversing fraction function

def exponentiating():
    while True:
        try:
            x = input("input fraction A\n")
            e = int(input("enter exponent\n"))
            x1, x2 = mixed_to_improper(x)
            x1 = x1**e
            x2 = x2**e
            x1, x2 = simplify(x1, x2)
            x = improper_to_mixed(x1, x2)
            return (x)
        except:
            print("please enter a valid input")
#line 157-169 is my exponentiating fraction function

if __name__ == '__main__':
    print_menu()
    n = menu_selection()
    if n == 5:
        answer = inversing()
    elif n == 6:
        answer = exponentiating()
    else:
        x1, x2, y1, y2 = get_input()
        if n == 1:
            p1, p2 = add_frac(x1, x2, y1, y2)
        elif n == 2:
            p1, p2 = sub_frac(x1, x2, y1, y2)
        elif n == 3:
            p1, p2 = multiply_frac(x1, x2, y1, y2)
        elif n == 4:
            p1, p2 = divide_frac(x1, x2, y1, y2)
            p1, p2 = simplify(p1, p2)
        if p1 == 0:
            answer = p1
        answer = improper_to_mixed(p1, p2)

    print(answer)
#line 172-194 executes my code
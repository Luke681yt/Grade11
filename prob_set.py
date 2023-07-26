def print_menu():
    print("1-get number of solutions\n2-get point of intersection\n3-quit")

def get_menu_selection():
    print_menu()
    while True:
        n=int(input())
        if n>0 and n<3:
            return n
        elif n==3:
            print("quitting")
            return n
        else:
            print("invalid input")
#line 1-15 is the function that prints the menu and gets the input

def get_input():
    line1=input("enter line 1\n")
    line2=input("enter line 2\n")
    return(line1,line2)
#my get input function to get line 1 and line 2

#A and C are slope B and D are y intercepts
def no_of_solutions(a,b,c,d):
    a,b,c,d=int(a),int(b),int(c),int(d)
    if a==c and b!=d:
        return(0)
    elif a==c and b==d:
        return("infinetly many solutions")
    elif a!=c:
        return("one solution")


def point_of_intersection(a,b,c,d):
    a,b,c,d=int(a),int(b),int(c),int(d)
    if a==c:
        return("None")
    else:
        x=round(((d-b)/(a-c)),2)
        y=round(((((a*d)-(a*b))/(a-c))+b),2)
        poi=x,y
        return poi


#line 17-28 are my number of solutions and my point of intersection function

def get_slope(line):
    equal=line.find("=")
    x=line.find("x")
    m=line[equal+1:x]
    try:
      m=int(m)
      assert m!=None
      return m
    except:
        return 1
       
def get_y(line):
    x=line.find("x")
    y=line[x+1:]
    try:
      y=int(y)
      assert y!=None 
      return y
    except:
        return 0

#input is y=ax+b i need to index a and b, + or 0
def get_abcd(line1,line2):
    line1=line1.strip()
    line2=line2.strip()
    a=get_slope(line1)
    c=get_slope(line2)
    b=get_y(line1)
    d=get_y(line2)
    return a,b,c,d
#turning line1 and line2 into a,b,c,d

if __name__ == '__main__':
    n=get_menu_selection()
    if n==3:
        print("successfully closed program")
    else:
        line1,line2=get_input()
        a,b,c,d=get_abcd(line1,line2)
        if n==1:
            print(no_of_solutions(a,b,c,d))
        if n==2:
            print(point_of_intersection(a,b,c,d))

#printing my code and executing it
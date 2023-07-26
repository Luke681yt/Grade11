def print_menu():
    print("1-add AB and CD\n2-subtract AB and CD\n3-multiply AB and CD\n4-divide AB and CD\n5-inversing\n6-exponentiating")
def menu_selection():
    while True:
        try:
            n=input("enter menu selection:\n")
            if int(n)>0 and int(n)<7:
                return int(n)
        except:
            print("enter a valid input\n")

def mixed_to_improper(f):
    try:
        space=f.find(" ")
        slash=f.find("/")
        px=f[:space]
        p1=f[space+1:slash]
        p2=f[slash+1:]
        p1=int(p1)
        p2=int(p2)
        px=int(px)
        p1=((p2*px)+p1)
        return p1,p2
    except:
        try:
            slash=f.find("/")
            p1=f[:slash]
            p2=f[slash+1:]
            p1=int(p1)
            p2=int(p2)
            return p1,p2
        except:
            print("invalid input")
def improper_to_mixed(p1,p2):
    if abs(p1)<abs(p2):
        mx=0.01
        return mx,p1,p2
    elif p1>0 and p2>0 or p1<0 and p2<0:
        mx=abs(p1)//abs(p2)
        p1=abs(p1)-(abs(p2)*mx)
        return(mx,p1,abs(p2))
    elif abs(p1)>abs(p2):
        if p1<0 or p2<0:
            neg=True
        mx=abs(p1)//abs(p2)
        p1=abs(p1)-(mx*(abs(p2)))
        if neg==True:
            mx=-1(mx)
            return mx,p1,abs(p2)
        
def simplify(p1,p2):
    for i in range(p2,0,-1):
        if p1%i==0 and p2%i==0:
            p1=p1/i
            p2=p2/i
            return p1,p2
    return p1,p2

def get_input():
         while True:
            x=str(input("input fraction A\n"))
            y=str(input("input fraction B\n"))
            try:
                x1,x2=mixed_to_improper(x)
                y1,y2=mixed_to_improper(y)
                return(x1,x2,y1,y2)
            except:
                print("please enter a valid input")

def add_frac(x1,x2,y1,y2):
    x1=int(x1)
    x2=int(x2)
    y1=int(y1)
    y2=int(y2)
    if x2==y2:
        p1=x1+y1
        p2=x2
        return p1,p2
    elif x2!=y2:
        p2=x2*y2
        p1=(x1*y2)+(y1*x2)
        return p1,p2

def sub_frac(x1,x2,y1,y2):
    x1=int(x1)
    x2=int(x2)
    y1=int(y1)
    y2=int(y2)
    if x2==y2:
        p1=x1-y1
        p2=x2
        return p1,p2
    elif x2!=y2:
        p2=x2*y2
        p1=(x1*y2)-(y1*y2)
        return p1,p2

def multiply_frac(x1,x2,y1,y2):
    x1=int(x1)
    x2=int(x2)
    y1=int(y1)
    y2=int(y2)
    p1=x1*y1
    p2=x2*y2
    return p1,p2

def divide_frac(x1,x2,y1,y2):
    x1=int(x1)
    x2=int(x2)
    y1=int(y1)
    y2=int(y2)
    p1=x1*y2
    p2=x2*y1
    return p1,p2

def inversing():
        while True:
            try:
                x=input("input fraction A\n")
                x1,x2=mixed_to_improper(x)
                x1,x2=simplify(x1,x2)
                x=improper_to_mixed(x2,x1)
                return(x)
            except:
                print("invalid input")

def exponentiating():
    while True:
        try:
            x=input("input fraction A\n")
            e=int(input("enter exponent\n"))
            x1,x2=mixed_to_improper(x)
            x1=int(x1)
            x2=int(x2)
            x1=x1**e
            x2=x2**e
            x1,x2=simplify(x1,x2)
            x1,x2,mx=improper_to_mixed(x1,x2)
            return(x1,x2,mx)
        except:
            print("please enter a valid input")

if __name__ == '__main__':
    print_menu()
    n=menu_selection()
    if n==5:
            answer=inversing()
    elif n==6:
            p1,p2,mx=exponentiating()
    else:
        x1,x2,y1,y2=get_input()
        if n==1:
            p1,p2=add_frac(x1,x2,y1,y2)
        elif n==2:
            p1,p2=sub_frac(x1,x2,y1,y2)    
        elif n==3:
            p1,p2=multiply_frac(x1,x2,y1,y2)
        elif n==4:
            p1,p2=divide_frac(x1,x2,y1,y2)
            p1,p2=simplify(p1,p2)
        if p1==0:
            print("no output")
    if mx==0.01:
      print(p1,p2)
    else:
        print(mx,p1,p2)



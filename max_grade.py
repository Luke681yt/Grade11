#a=#of students 
#b= grade, mark
a=int(input("# of students?\n"))
current_max9=0
current_max10=0
current_max11=0
current_max12=0

for i in range(a):
    b=input('enter grade and mark as "grade, mark"\n ')
    comma=b.index(",")
    grade=int(b[0:comma])
    mark=int(b[comma+1:-1])
    if grade==9:
        if mark>current_max9:
            current_max9=mark
    if grade==10:
        if mark>current_max10:
            current_max10=mark
    if grade==11:
        if mark>current_max11:
            current_max11=mark
    if grade==12:
        if mark>current_max12:
            current_max12=mark
print(current_max9, current_max10, current_max11, current_max12)


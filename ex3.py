#get letter inputs and math to a grade than give an average
num=input("enter no of grades fr ong\n")
accum=float(0)
for i in range(num):
    letter_grade=input("enter letter grade:\n")
    if letter_grade=="A+":
        accum=accum+4
    if letter_grade=="A":
        accum=accum+4
    if letter_grade=="A-":
        accum=accum+3.7
    if letter_grade=="B+":
        accum=accum+3.3
    if letter_grade=="B":
        accum=accum+3
    if letter_grade=="B-":
        accum=accum+2.7
    if letter_grade=="C+":
        accum=accum+2.3
    if letter_grade=="C":
        accum=accum+2
    if letter_grade=="C-":
        accum=accum+1.7
    if letter_grade=="D+":
        accum=accum+1.3
    if letter_grade=="D":
        accum=accum+1
    if letter_grade=="F":
        accum=accum+0
print(round(accum/num, 1))
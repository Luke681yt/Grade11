#for loops are used to repeat code
#i means index
# range(10) gives a "list" of 10 numbers from 0-9
for i in range(10):
    print("hi")

for i in range(15):
    print(i)

#print all numbers from 0-10

for i in range(2, 11):
    print(i)

for i in range(0, 101, 5): #range(0, 101, 5) gives a list of every 5 numbers 0-100 (not including 101!!)
    print(i)

for i in range(10, -1, -1):
    print(i)

for i in range(5):
    print("*****")

print("______________________________________________")

for i in range(5): #0,1,2,3,4
    print((5-i) * "*") # printing 5-i stars

print("_______________________________")

for i in range(1,8,2): #1,3,5,7
    print(i*"*")
for i in range(5,0,-2):
    print(i*"*")

print("_____________________")

for i in range(8,1,-2):
    print(i*"*")
for i in range(3,9,2):
    print(i*"*")
print("____________________")
for j in range(-5,3,2):
    print(j)
print("___________")
#take in a num from 1-50 and output all factors
integr=int(input("input num"))
for num in range(1,51):
    if integr/num == integr//num:
        print(num)


#phrase=input("enter thing here idekl\n")
#if phrase[::-1] == phrase:
#    print("is a palindrome")
#else:print("not a palindrome")

#take in no of students take in name and mark, output highest name/names and mark
studs=int(input())
mark=0
topmark=0

for i in range(studs):
    name=input()
    mark=int(input())
    if mark > topmark:
        topmark=mark
        accum=name
    elif mark < topmark:
        topmark=topmark
    elif mark==topmark:
        accum=(f"{accum}, {name}")
print(accum)
print(topmark)
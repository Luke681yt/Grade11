#30 characters max made up of I,O,S,H,Z,X and N all uppercase
word=input("enter word n ill check ok good bye\n")
length=0
for i in word:
    if len(word)>30:
        print("NO")
    elif i in "IOSHZXN":
        length=length+1
if length==(len(word)):
    print("YES")
else:
    print("NO")
    
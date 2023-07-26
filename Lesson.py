#upper case letter, number, symbol, length 7-13
password=input()
accum=""
uppercase=False
number=False
symbol=False
length=False

for i in range(len(password)):
    if password[i].isupper():
        uppercase=True
    elif password[i].isnumeric():
            number=True
    elif password[i] in "@#$%^&*":
        symbol=True
if len(password)>6 and len(password)<14:
    length=True
if length and symbol and uppercase:
    print("valid")
else:
    print("invalid")
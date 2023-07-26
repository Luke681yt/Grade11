# converts decimal to the next base between 2 and 9

def dec_to_base(n,b):
    accum=""
    r=0
    while n>0:
        r=n%b
        accum=str(r)+accum
        n=n//b
    return accum

print (dec_to_base(382,8))

def base_to_dec(n,b):
    accum=0
    i=0
    for digit in str(n):
        accum=accum+int(digit) * b ** ((len(str(n)))-1-i)
        i+=1
    return accum

print(base_to_dec(101,2))

def from_hex(n):
    hex="123456789ABCDEF"
    base10=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    exp=0
    accum=0
    for i in str(n)[::-1]:
        digit=hex.find(i)
        new_digit=base10[digit]
        accum+=new_digit*(16**exp)
        exp+=1
    return accum

print (from_hex("7D"))

def to_hex(n):
    r=0
    accum=""
    hex="123456789ABCDEF"
    
'''In a new file write two functions hex_to_dec(hexadecimal) and dec_to_hex(decimal). The first function takes in 
a positive integer that represents a hexadecimal and returns a decimal value. The second function takes in a positive integer 
that represents a decimal value and returns a hexadecimal.'''

#0123456789ABCDEF
#A=10
#B=11
#C=12
#D=13
#E=14
#F=15

# F     5     D     2
# 16^3  16^2  16^1  16^0

#= 15 * 16^3 + 5 * 16^2 + 13 * 16^1 + 2 * 16^0

def hex_to_dec(hex):
    # hex will already be a string
    # going through digits backwards
    result = 0
    exp = 0
    for digit in hex[::-1]:
        if digit in "ABCDEF":
            number = "ABCDEF".index(digit) + 10
        else:
            number = int(digit)    
        result += number * 16 ** exp
        exp += 1
    return result

print(hex_to_dec("FD5"))
print(5 * 1 + 13 * 16 + 15 * 16 ** 2)

def dec_to_hex(dec):
    quotient = dec
    remainders = ""
    # keep going until quotient is 0
    while quotient != 0:
        remainder = quotient % 16
        # integer division to get whole number
        quotient = quotient // 16
        if remainder >= 10:
            letter = "ABCDEF"[remainder - 10]
        else:
            letter = str(remainder)
        remainders += letter
    # reverse the remainders for the answer
    return remainders[::-1]
print(dec_to_hex(hex_to_dec("FA1245")))

for digit in str(1234567):
    print(digit)

def to_hex(n):
    hex="123456789ABCDEF"
    r=0
    accum=""
    while n>0:
        r=n%16
        digit=hex[r-1]
        accum=digit+accum
        n=n//16
    return accum

def to_binary(n):
    accum=""
    r=0
    while n>0:
        r=n%2
        accum=str(r)+accum
        n=n//2
    return accum

def from_binary(n: str):
    accum=0
    n=n[::-1]
    for i in range(len(n)):
        digit=n[i]*(2**i)
        accum=accum+digit
    return accum

def from_bin(n: str):
    accum=0
    n=n[::-1]
    for i in range(len(n)):
        digit=n[i]
        accum=accum+int(digit)*(2**i)
    return accum

def from_hexa(n):
    result=0
    exp=0
    for digit in n[::-1]:
        if digit in "ABCDEF":
            num="ABCDEF".index(digit)+10
        else:
            num=int(digit)
        result+=num*(16**exp)
        exp+=1
    return result

print(to_hex(702545))


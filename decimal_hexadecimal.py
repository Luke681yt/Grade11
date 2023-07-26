def to_hexa(n):
    hex="123456789ABCDEF"


def from_hexa(n):
    print(2)

def to_bin(n):
    r=0
    accum=""
    while n>0:
        r=n%2
        accum=str(r)+accum
        n=n//2
    return(accum)

def from_bin(n):
    print(4)

print(to_bin())
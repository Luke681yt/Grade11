#number to binary
def num_to_bin(number):
    accum=str(0)
    quotient=0
    while number!=0:
        quotient=number//2
        if number%2==0:
            accum=accum+"0"
        if number%2==1:
            accum=accum+"1"
        number=quotient
    accum=accum[1:]
    accum=accum[::-1]
    return accum

print(num_to_bin(9234))

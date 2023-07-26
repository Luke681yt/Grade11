#convert num to binary
def num_to_bin(binary):
    result=0
    exponent=0
    for i in str(binary)[::-1]:
        result+=int(i)*2**exponent
        exponent+=1
    return result

a=int(input("enter binary\n"))
print(num_to_bin(a))
        


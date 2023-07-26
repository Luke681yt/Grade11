x=int(input("enter number"))
n=int(input("enter number"))
accum=0
for i in range(n+1):
    accum=accum+(x**(n-i))
print(accum)
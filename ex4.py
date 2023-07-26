a=int(input())
d=int(input())
n=int(input())
accum=0
for i in range(n):
    accum=accum+(a+(i*d))
print(accum)
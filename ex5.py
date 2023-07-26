n=int(input("input how many numeros of the fibonnica thing you want fr"))
a=1
b=1
s=0
accum=0
for i in range(n):
    print(a)
    s=s+a
    temp=b
    b=a+b
    a=temp

print(s)

import random

def geometric(n,b):
    f=0
    for i in range(n+1):
        f+=(b**i)
    return f

b=random.randint(1,200)
n=random.randint(1,250)
print(geometric(n,b))
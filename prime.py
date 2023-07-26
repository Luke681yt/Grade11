import random

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def random_prime(a,b):
    n=random.randint(a,b)
    while not is_prime(n):
        n=random.randint(a,b)
    return n

for i in range(1000):
    print(random_prime(1,100000))
import random
ht=input("ENTER H OR T")
flips=int(input("emnter flips # loser"))
coins=["H","T"]
h=""
k=""
counter=-1
clongest=1
longest=1
for i in range(flips):
    h=random.choice(coins)
    if h==k:
        clongest+=1
    elif h!=k:
        longest=clongest
        clongest=1
    print(h)
    if k!=h:
        counter+=1
    k=h
print("amount of times switched",counter)
print("Longest streak", longest)
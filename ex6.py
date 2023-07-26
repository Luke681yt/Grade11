a=input()
con=""
for i in (a):
    if i in "aeiouAEIOU":
        pass
    else:
       con=con+i
con=con[::-1]
print(con)

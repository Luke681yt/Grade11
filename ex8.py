sentence=input("enter setnecne fr\n")
shift=int(input("enter nom u wanna be sifted by fr]n"))
alphabet="abcdefghijklmnopqrstuvwxyz"
lphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
accum=""
for char in sentence:

    if char in alphabet:
      c=(alphabet.index(char))
      f=(c + shift)%26
      b=alphabet[f]
      accum=accum+b
print(accum)
#    elif char in lphabet:
#       b=lphabet[f+shift]
#       accum=accum+b
#    else:
#        accum=accum+char
#print(accum)
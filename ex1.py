sen=input()
shift=13
accum=""
alphabetcap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetlower="abcdefghijklmnopqrstuvwxyz"
for i in sen:
    if i in alphabetlower:
        l=alphabetlower.index(i)

        accum=accum+(alphabetlower[(l+shift)%26])
    elif i in alphabetcap:
        l=alphabetcap.index(i)
        accum=accum+(alphabetcap[(l+shift)%26])
    elif i==" ":
        accum=accum+i

for i in accum:
    if i.lower()=="a":
        i=1


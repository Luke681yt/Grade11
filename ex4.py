import doctest

def remove_vowels(string):
    accum=""
    for i in string:
        if i in "AEIOUaeiou":
            pass
        else:
            accum=accum+i
    return accum

def count_vowels(string):
    total=0
    for i in string:
        if i in "aeiouAEIOU":
            total+=1
    return total

print(remove_vowels("aweyitoru"))

def reverse_case(string):
    """(string) -> (string)
    reverses the string
    >>> reverse_case("abcdefg")
    "gfedcba"""
    accum=""
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if i in upper:
            loc=upper.index(i)
            accum=accum+lower[loc]
        elif i in lower:
            loc=lower.index(i)
            accum=accum+lower[loc]
    return accum

if __name__=="__main__":
    doctest.testmod()
    reverse_case("ABCDEFG")
#add ub before each vowel
str=input("enter characters here:\n")
accum=""
for letter in str:
    if letter.lower() in "aeiou":
        accum=accum + "ub" + letter
    elif letter.isalpha and letter not in "aeiou":
        accum= accum + letter
print(accum)

#write a program that takes in a sentence and outputs the sentence with reverse casing (A -> a) (b -> B)
sentence=input("here:\n")
accum=""
for char in sentence:
    if char.islower():
        accum=accum+char.upper()
    elif char.isupper():
        accum=accum+char.lower()
    else:
        accum=accum+char
print(accum)

def count_occurances(string,item):
    counter=0
    for i in string:
        if i==item:
            counter+=1
    return counter

print(count_occurances("I like chimpanzees","e"))
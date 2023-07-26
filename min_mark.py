num_of_ints=int(input())
for i in range(num_of_ints):
    number=int(input("enter an integer"))
    if i == 0:
        current_max= number
        current_min= number
else:
    if number> current_max:
        current_max=number
    if number< current_min:
        current_min=number
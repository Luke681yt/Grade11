item_cost=0
sub_total=0
num_of_items=0
while item_cost!=(-1):
    item_cost=float(input())
    if item_cost!=(-1):
        sub_total=sub_total+item_cost
        num_of_items=num_of_items+1
    else:
        continue
print("sub total: ","%.2f" % (sub_total))
print("total: ","%.2f" %( sub_total*1.13))
print("Average cost:  ","%.2f" %(sub_total/num_of_items))
#"%.2f" %
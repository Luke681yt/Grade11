#4 digit is randomly generated and cannot have any duplicates
import random
correct_check=0 
sec_num=random.randint(1000, 9999)
print(sec_num)
sec_num=str(sec_num)
while sec_num[0]==sec_num[1] or sec_num[0]==sec_num[2] or sec_num[0]==sec_num[3] or sec_num[1]==sec_num[2] or sec_num[1]==sec_num[3] or sec_num[2]==sec_num[3]:
        sec_num=random.randint(1000, 9999)
        sec_num=str(sec_num)

print(sec_num)
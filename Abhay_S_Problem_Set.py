8796
#user has 5 tries to guess a 4 digit number, it will give desc for each number, "in number not right place", "in the right place", "not in number"
#4 digit is randomly generated and cannot have any duplicates
import random
correct_check=0 
sec_num=random.randint(1000, 9999)
sec_num=str(sec_num)
while sec_num[0]==sec_num[1] or sec_num[0]==sec_num[2] or sec_num[0]==sec_num[3] or sec_num[1]==sec_num[2] or sec_num[1]==sec_num[3] or sec_num[2]==sec_num[3]:
        sec_num=random.randint(1000, 9999)
        sec_num=str(sec_num)
# in line 4 I setup an accumulator to check if the user won or lost the game
#in line 6-9 I generated a random 4 digit number and used a while loop to re-generate the number if any digits were the same


for i in range(5):
    user_guess=str(input())

    if user_guess[0]==sec_num[0]:
        print(user_guess[0]," is the correct number")
        correct_check=correct_check+1
    elif user_guess[0] in sec_num:
        print(user_guess[0], " is in the number but not in the correct spot")
    else:
        print(user_guess[0], " is not in the number")

#in line 14 I set the range to 5 because the user gets only 5 guesses333

#in line 19 I add one to the correct check if the numbers match on the dot, I did this for all numbers so that if correct_check==4 than the number the user inputted was correct and the game is over

# in line 17-23 I checked if the first letter the user inputted matched the secret number, if it was even in it, or if it wasnt and gave an appropriate output

    if user_guess[1]==sec_num[1]:
        print(user_guess[1]," is the correct number")
        correct_check=correct_check+1
    elif user_guess[1] in sec_num:
        print(user_guess[1], " is in the number but not in the correct spot")
    else:
        print(user_guess[1], " is not in the number")

#in line 31-37 I checked if the second digits lined up or if they were off and gave an appropriate response

    if user_guess[2]==sec_num[2]:
        print(user_guess[2]," is the correct number")
        correct_check=correct_check+1
    elif user_guess[2] in sec_num:
        print(user_guess[2], " is in the number but not in the correct spot")
    else:
        print(user_guess[2], " is not in the number")

#in line 41-47 I checked if the 3rd digit lined up or if it was off and gave the appropriate response

    if user_guess[3]==sec_num[3]:
        print(user_guess[3]," is the correct number")
        correct_check=correct_check+1
    elif user_guess[3] in sec_num:
        print(user_guess[3], " is in the number but not in the correct spot")
    else:
        print(user_guess[3], " is not in the number")
    
#I checked if digits matched for the 4th digit in both numbers and gave the appropriate response

    if correct_check==4:
        print("Great job,\nPlease play again soon!")
        break
    elif correct_check<4:
        correct_check=0

#in line 61-65 I checked if the user had won using the correct check i setup, and if the user didn't I reset correct check to 0 for their next playthrough

if correct_check!=4:  
    print("sorry, you lost!\nbetter luck next time!")

#after the forloop had ended I checked if correct_check!=4, and then said the user lost because of it
#I didn't check for victory (correct_check==4) because in line 60 (inside the forloop) I said break so that when the user wins the game ends

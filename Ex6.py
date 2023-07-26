import random
user=""
comp_wins=0
per_wins=0
game=["rock","paper","scizzors"]
while user!="quit":
    user=input("enter rock, paper or scizzors:\n")
    comp=random.choice(game)
    if user=="rock" and comp=="scizzors":
        per_wins+=1
        print("computer picked !\n","you won :)")
    if user=="paper" and comp=="rock":
        per_wins+=1
        print("computer picked rock!\n","you won :)")
    if user=="scizzors" and comp=="paper":
        per_wins+=1
        print("computer picked paper!\n","you won :)")
    if user=="scizzors" and comp=="rock":
        comp_wins+=1
        print("computer picked rock!\n","you lost :(")
    if user=="rock" and comp=="paper":
        comp_wins+=1
        print("computer picked paper!\n","you lost :(")
    if user=="paper" and comp=="scizzors":
        print("computer picked scizzors!\n","you lost :(")
        comp_wins+=1
    if user==comp:
        print("tie!\n","comp picked ",comp)
print("computer wins: ", comp_wins)
print("user wins:  ", per_wins)

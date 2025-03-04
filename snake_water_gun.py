import random

def check_score(computer,user):
    if computer == user:
        return 0
    if (computer ==0 and user == 1):
        return -1
        
    if computer==1 and  user ==2:
        return -1
        
    if computer == 2 and user ==0:
        return -1
    
    return 1 
computer=random.randint(0,2)
user = int(input("Enter 0 for Snake, 1 for Water, 2 for Gun: \n"))
if user  not in [0,1,2]:
    print("Invalid Input")
    exit()
score = check_score(computer,user)
print("You: ",user)
print("computer: ",computer)

if score ==0:
    print("Draw")
elif score == -1:
    print("You Lost")
else:
    print("Yay! You won :)")

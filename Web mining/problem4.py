import random
Choose=input("Choose: ")
computer_object=random.choice(["paper","rock","scissors"])
#print(computer_object)
if computer_object!=Choose:
    if Choose=="paper":
        if computer_object=="scissors":
            print("The computer chose scissors. The computer wins :(")
        elif computer_object=="rock":
            print("The computer chose rock. You win!")
    elif Choose=="rock":
        if computer_object=="paper":
            print("The computer chose paper. The computer wins :(")
        elif computer_object=="scissors":
            print("The computer chose scissors. You win!")
    elif Choose=="scissors":
        if computer_object=="paper":
            print("The computer chose paper. You win!")
        elif computer_object=="rock":
            print("The computer chose rock. The computer wins :(")
else:
    print("The computer chose {}. Let's settle this.".format(computer_object))

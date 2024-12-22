"""Create a Python program that greets the user with the message "Welcome to
the Space Mission". Then, ask the user whether they want to go "to the moon"
or "to Mars". If they choose "to Mars", print "Game Over". If they choose "to
the moon", ask if they want to "land on the surface" or "stay in orbit". If they
choose "land on the surface", print "Game Over". If they choose "stay in orbit",
ask them to choose between "alien", "asteroid", or "satellite". If they choose
"alien" or "asteroid", print "Game Over". If they choose "satellite", print "You
Win"."""
print("Welcome to the Space Mission!!")
choice=input("Do you want to the 'Moon' or 'Mars'?  ")
if choice=="Mars":
    print("Game Over")
elif choice=="Moon":
    path=input("Want to Land on surface or stay in orbit? type 'L' for surface and 'S' for orbit:  ")
    if path=="L":
        print("Game Over")
    elif path=="S":
        choice_user=input("choose 0 for 'alien', 1 for 'asteroid' and 2 for 'satellite': ")
        if choice_user=="0" or choice_user=="1":
            print("Game Over")
        elif choice_user=="2":
            print("You win")
        else:
            print("Invalid number for chosing.")
else:
    print("Invalid user choice.Thanks for playing.")
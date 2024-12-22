"""Create a Python program that greets the user with the message "Welcome to
the Haunted House". Then, ask the user whether they want to go "upstairs" or
"downstairs". If they choose "downstairs", print "Game Over". If they choose
"upstairs", ask if they want to "enter the room" or "stay outside". If they choose
"enter the room", print "Game Over". If they choose "stay outside", ask them
to choose between "ghost", "vampire", or "werewolf". If they choose "ghost" or
"vampire", print "Game Over". If they choose "werewolf", print "You Win"."""
print("Welcome to the vampire house!")
up_down=input("Do you want to go upstairs or downstairs? ")
if up_down=="downstairs":
    print("Game Over")
elif up_down=="upstairs":
    stay=input("press E for 'enter the room' and O for 'stay outside' : ")
    if stay=="E":
        print("Game Over")
    elif stay=="O":
        choice_user=input("choose 0 for 'ghost', 1 for 'vampire' and 2 for 'werewolf': ")
        if choice_user=="0" or choice_user=="1":
            print("Game Over")
        elif choice_user=="2":
            print("You win")
        else:
            print("Invalid number for chosing.")
else:
    print("Invalid user choice.Thanks for playing.")
        

""" Create a Python program that greets the user with the message "Welcome to
the Pirate Island". Then, ask the user whether they want to go "left" or "right".
If they choose "right", print "Game Over". If they choose "left", ask if they want
to "dig for treasure" or "sail the ship". If they choose "dig for treasure", print
"Game Over". If they choose "sail the ship", ask them to choose between
"shark", "pirate ship", or "mermaid". If they choose "shark" or "pirate ship",
print "Game Over". If they choose "mermaid", print "You Win"."""
print("Welcome to the Pirate Island!!")
choice=input("Do you want to the 'left' or 'right'?  ")
if choice=="right":
    print("Game Over")
elif choice=="left":
    path=input("Want to dig for treaure or sail the ship? type 'D' for digging and 'S' for sailing:  ")
    if path=="D":
        print("Game Over")
    elif path=="S":
        choice_user=input("choose 0 for 'shakr', 1 for 'pirate ship' and 2 for 'mermaid': ")
        if choice_user=="0" or choice_user=="1":
            print("Game Over")
        elif choice_user=="2":
            print("You win")
        else:
            print("Invalid number for chosing.")
else:
    print("Invalid user choice.Thanks for playing.")
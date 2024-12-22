"""Create a Python program that greets the user with the message "Welcome to
the Magic Forest". Then, ask the user whether they want to go "north" or
"south". If they choose "south", print "Game Over". If they choose "north", ask
if they want to "cross the river" or "follow the path". If they choose "cross the
river", print "Game Over". If they choose "follow the path", ask them to choose
between "fairy", "ogre", or "elf". If they choose "ogre" or "fairy", print "Game
Over". If they choose "elf", print "You Win"."""
print("Welcome to the magic forest!!")
direction=input("Do you want to go north or south? type 'N' for north and 'S' for South':  ")
if direction=="S":
    print("Game Over")
elif direction=="N":
    path=input("Want to cross the river or follow the path? type 'C' for crossing and 'F' for following: ")
    if path=="C":
        print("Game Over")
    elif path=="F":
        choice_user=input("choose 0 for 'fairy', 1 for 'ogre' and 2 for 'elf': ")
        if choice_user=="0" or choice_user=="1":
            print("Game Over")
        elif choice_user=="2":
            print("You win")
        else:
            print("Invalid number for chosing.")
else:
    print("Invalid user choice.Thanks for playing.")
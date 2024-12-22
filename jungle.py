"""Create a Python program that greets the user with the message "Welcome to
the Jungle Adventure". Then, ask the user whether they want to go "left" or
"right". If they choose "right", print "Game Over". If they choose "left", ask if
they want to "climb a tree" or "explore the cave". If they choose "climb a tree",
print "Game Over". If they choose "explore the cave", ask them to choose
between "bear", "tiger", or "snake". If they choose "bear" or "tiger", print
"Game Over". If they choose "snake", print "You Win"."""
print("Welcome to the jungle adventure!!")
right_left=input("Do you want to go right or left? type 'R' for right and 'L for left':  ")
if right_left=="R":
    print("Game Over")
elif right_left=="L":
    explore_climb=input("Want to climb tree or explore the cave? type 'C' for climbing and 'E' for exploring: ")
    if explore_climb=="E":
        print("Game Over")
    elif explore_climb=="C":
        choice_user=input("choose 0 for 'bear', 1 for 'tiger' and 2 for 'snake': ")
        if choice_user=="0" or choice_user=="1":
            print("Game Over")
        elif choice_user=="2":
            print("You win")
        else:
            print("Invalid number for chosing.")
else:
    print("Invalid user choice.Thanks for playing.")
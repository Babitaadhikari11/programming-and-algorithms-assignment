# Write a program to accept percentage and display the result

obtain_percent=eval(input("Enter your marks in [%]: "))
if obtain_percent>0:
    if obtain_percent>=65:
        print("Excellent")
    elif obtain_percent>=55 and obtain_percent<65:
        print("Good")
    elif obtain_percent>=40 and obtain_percent<55:
        print("Fair")
    elif obtain_percent<40:
        print("Failed")
else:
    print("Please enter a postive value of marks")
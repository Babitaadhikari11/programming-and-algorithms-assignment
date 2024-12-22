#  A program to take two numbers and find the greater of the two. If they are equal, check if the number is positive, negative, or zero.
num_1=eval(input("Enter a first number: "))
num_2=eval(input("Enter a second number: "))
if num_1==num_2:
    if num_1>0:
        print("The integers are positive and equal.")
    elif num_1<0:
        print("The integers are negative and equal.")
    else:
        print("The integers are zero.")
else:
    if num_1>num_2:
        print(F"{num_1} is greater")
    else:
        print(F"{num_2} is greater")
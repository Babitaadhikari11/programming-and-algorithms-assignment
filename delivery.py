# Write a program to calculate the delivery cost based on the weight of the package
weight=eval(input("Enter the weight of package in [KG]: "))
charge=0
if weight<5:
    charge=5
if weight>=5 and weight<=20:
    charge=10
    urgency=input("Is the delivery urgent? 'yes/no':" )
    if urgency=="yes":
         charge+=5
    elif urgency=="no":
        charge=10
elif weight>20:
    charge=20
print(f"The delivery cost based on weight of package is : {charge}")

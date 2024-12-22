# Write a python program which accepts the radius of circle from user and compute the area.
radius=eval(input('Enter the value of radius in [cm]: '))
if radius>0:
    area=float(3.14*radius**2)
    print(f"The area of given circle is : {area}cm.")
else:
    print("Please enter the positive value of radius")

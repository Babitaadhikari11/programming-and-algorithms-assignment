# A program to accept the grades from the user and display the grade
grade=eval(input("Enter the marks in percentage[%]: "))
if grade>80:
    print("A+")
elif grade <= 80 and grade > 60:
    print("A")
elif grade<=60 and grade > 50:
    print("B+")
elif grade<=50 and grade > 45:
    print("B")
elif grade<=45 and grade > 25:
    print("C")
elif grade<25:
    print("D")



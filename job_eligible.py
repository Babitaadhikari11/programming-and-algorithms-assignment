#  A program to determine if a candidate is eligible for a job: If the candidate's age is >= 18, check if they have a degree.
age=int(input("Enter the age of candidate: "))
if age>=18:
    degree=eval(input("Enter the degree of candidate: "))
    if degree>3:
        print("Highly Eligible")
    elif degree>1 and degree<=3:
        print("Eligible")
    else:
        print("Under Review")
else:
    print("Age must be above 18")
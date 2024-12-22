# A company decided to give bonus of 5% to employee if his/her year ofservice is more than 5years. Ask user for their salary and year of service and print the net bonus amount.
 

year=eval(input("Enter the working year: "))
if year>5:
    salary=eval(input("Enter the salary in Rs: "))
    bonus=5/100
    total=float(salary*bonus)
    print(f"{total}")
else:
    print("Employee hasn't worked for 5 years")
# A company decided to give bonus to employee 

year=eval(input("Enter the working year: "))
salary=eval(input("Enter the salary in Rs: "))
if year>10:
    bonus=10/100
elif year>=6 and year<=10:
    bonus=8/100
elif year<6:
    bonus=5/100
total=float(salary*bonus)
print(f"{total}")
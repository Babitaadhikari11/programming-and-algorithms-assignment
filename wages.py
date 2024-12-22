# Accept the age, gender ('M', 'F'), number of days and display the wages
dict_1={1:"M",2:"F"}
age=int(input("Enter your age : "))
print(dict_1)
gender=(input("Enter 'M' for Male and 'F' for Female: "))
days=eval(input("Enter the number of days worked: " ))
if  age>=18 and age<30:
    if gender==dict_1[1]:
        wage=days*700
        print(f"The wage of working for {days} is Rs.{wage}")
    elif gender==dict_1[2]:
        wage=days*750
        print(f"The wage of working for {days} is Rs.{wage}")
elif age>=30 and age<=40:
    if gender==dict_1[1]:
        wage=days*800
        print(f"The wage of working for {days} is Rs.{wage}")
    elif gender==dict_1[2]:
        wage=days*850
        print(f"The wage of working for {days} is Rs.{wage}")

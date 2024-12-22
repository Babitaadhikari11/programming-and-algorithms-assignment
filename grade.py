# A program which accepts marks of four subjects and display total marks,percentage and grade.
sub_1=eval(input("Enter mark out of 100 [Mathematics]: "))
sub_2=eval(input("Enter mark out of 100 [Science]: "))
sub_3=eval(input("Enter mark out of 100 [Computer]: "))
sub_4=eval(input("Enter mark out of 100 [English]: "))
total_marks=400
obtained_marks=sub_1+sub_2+sub_3+sub_4
print(f"Obtained marks is : {obtained_marks}")
percentage=(obtained_marks/total_marks)*100
print(f"{percentage} %")
if percentage >=70:
    print("Distinction")
elif percentage >=60 and percentage <70:
    print("First Division")
elif percentage >=40 and percentage <60:
    print("Pass")
else:
    print("Fail")





   
    



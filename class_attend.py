# A program to accept the total number of days and absent from the user and calculate the percentage of class attended:
import math
total_student=int(input("Enter the total number of days of class: "))
absent=int(input("Enter the total absent days: "))
present=total_student-absent
if total_student>0:
    present_percentage=math.ceil((present/total_student)*100)
    total_in_percent=(total_student/total_student)*100
    if present_percentage>75:
        # print(f"you are present for {present_percentage}% out of 100%")
        print(f"You will be able to sit in the class as your present days [%] is : {present_percentage}%")
    elif present_percentage<75:
        print(f"You cannot sit in the exam as you have less present days [%] i.e. {present_percentage}%")
print(f"The absent percent is : {total_in_percent-present_percentage}%")

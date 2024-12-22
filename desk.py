# A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased. 
import math
class_one=int(input("Enter the total number of student in section 'A' : "))
class_two=int(input("Enter the total number of student in section 'B' : "))
class_three=int(input("Enter the total number of student in section 'C' : "))
desk_one=class_one/2
# if the students number is odd, one extra desk is required.
if class_one%2!=0:
        desk_one+=1
desk_two=class_two/2
if class_two%2!=0:
       desk_two+=1
desk_three=class_three/2
if class_three%2!=0:
        desk_three+=1
desk_total=desk_one+desk_two+desk_three
print(f"The total number of desk required for entire three classes is : {desk_total}")



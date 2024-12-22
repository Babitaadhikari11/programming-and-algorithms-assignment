# A program to read number of students and apple and print the total remained abd distributed apples
student=int(input("Enter the total number of students: "))
apple=int(input("Enter the total number of apples: "))
if apple%student!=0:
    distributed=(apple//student)
    print(f"The individual student gets {distributed} number of apples.")       
    remaining=apple%student
    print(f"The remaining apple in the basket is : {remaining}")

else:
    print("Not remained")

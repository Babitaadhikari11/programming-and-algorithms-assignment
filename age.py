# A program to accept the age of 4 people and display the eldest one
person_1=int(input("Enter the age of first person: "))
person_2=int(input("Enter the age of second person: "))
person_3=int(input("Enter the age of third person: "))
person_4=int(input("Enter the age of fourth person: "))
# if person_1<person_2 and person_1<person_3 and person_1<person_4:
#     print(f"{person_1} is the youngest one among 4 people.")
# elif person_2<person_1 and person_2<person_3 and person_2<person_4:
#     print(f"{person_2} is the youngest one among 4 people.")
# elif person_3<person_2 and person_3<person_1 and person_3<person_4:
#     print(f"{person_3} is the youngest one among 4 people.")
# elif person_4<person_2 and person_4<person_3 and person_4<person_1:
#     print(f"{person_4} is the youngest one among 4 people.")
# else:
#     print("Equal age")

if person_1>person_2 and person_1>person_3 and person_1>person_4:
    print(f"{person_1} is the eldest one among 4 people.")
elif person_2>person_1 and person_2>person_3 and person_2>person_4:
    print(f"{person_2} is the eldest one among 4 people.")
elif person_3>person_2 and person_3>person_1 and person_3>person_4:
    print(f"{person_3} is the eldest one among 4 people.")
elif person_4>person_2 and person_4>person_3 and person_4>person_1:
    print(f"{person_4} is the eldest one among 4 people.")
else:
    print("Equal age")
    
    
    
    
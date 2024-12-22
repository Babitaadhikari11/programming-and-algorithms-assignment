# A program to accept any city from the user and display monument of that city
array=["delhi","Agra","Jaipur"]
city=input("Enter the name of city : " )
if city == array[0]:
    print(f"The Red Fort is the monument of {array[0]}")
elif  city == array[1]:
    print(f"The Taj Mahal is the monument of {array[1]}")
elif city == array[2]:
    print(f"The Jal Mahal is the monument of {array[2]}")
else:
    print("No city found from the list")
""" Create a program that suggests activities based on the weather:
 If the weather is sunny, recommend outdoor activities like hiking or a picnic.
 If the weather is rainy, check if the user has a raincoat or umbrella:
    If yes, suggest going to a nearby mall or museum.
    If no, recommend staying home and watching movies"""
weather={1:"sunny",2:"rainy"}
weather_user=input("Enter the weather preference: ")
if weather_user==weather[1]:
    print("The weather is quite good for hiking or a picnic.")
elif weather_user==weather[2]:
    rainy=input("Do you have an umbrella or raincoat 'yes/no': ")
    if rainy=="yes":
        print("Its great idea to go nearby mall or museum.")
    elif rainy=="no":
        print("Stay at home and watch movies.")
else:
    print(f"We only provide choice for {weather[1]} and {weather[2]}!!")



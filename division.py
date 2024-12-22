# Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
num=int(input("Enter a number: "))
if num%2==0 and num%3==0:
    print(f"{num} is divisible by both the integers.")
else:
    print("Please enter a number which is divisible by 2 and 3.")
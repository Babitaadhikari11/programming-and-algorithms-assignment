# A program to accept the number of days from the user and calculate the charge for library
# day=eval(input("Enter the number of days to borrow the book: "))
# if day<=5:
#     # charge per day
#     charge=day*2
# elif day>=10 and day<=6:
#     charge=day*3
# elif day>=15 and day<=11:
#     charge=day*4
# elif day>15:
#     charge=day*5
# charged_amount=day*charge
# print(f"The total charged amount is Rs.{charged_amount}")

days = int(input("Enter the Number of Days :"))
if days>0 and days<= 5:
	charge = 2* days
	print("Fine Amount Pay to Rs :", charge)
 
elif(days >= 6 and days <= 10):
	charge = 3 * days
	print("Fine Amount Pay to Rs :", charge)
 
elif (days >=15 and days<=11):
	charge = 4 * days
	print("Fine Amount Pay to Rs :", charge)
elif days>15:
    charge = 5 * days
    print("Fine Amount Pay to Rs :", charge)

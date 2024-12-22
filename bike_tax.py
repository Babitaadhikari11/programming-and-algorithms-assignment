# A program to accept the cost price of a bike qnd display the road tax to be paid according to the following criteria:
# price=eval(input("Enter the cost price of bike in RS: "))
# tax_paid=eval(input("Enter the  rate of tax to be paid on each bike [Percentage]: "))
# tax_convert=(tax_paid/100)
# tax_amount=float(price*tax_convert)
# if price >100000:
#     print(f"Rs.{tax_amount} tax amount is paid.")
# elif price>50000 and price <=100000:
#     print(f"Rs.{tax_amount} tax amount is paid.")
# elif price<=50000:
#     print(f"Rs.{tax_amount} tax amount is paid.")
    

# A program to accept the cost price of a bike qnd display the road tax to be paid according to the following criteria:
price=eval(input("Enter the cost price of bike in RS: "))
if price >100000:
    tax_rate=0.15
elif price>50000 and price <=100000:
    tax_rate = 0.10  
elif price<=50000:
    tax_rate = 0.5
tax = float(price * tax_rate)
print(f"The road tax to be paid is Rs {tax}:")

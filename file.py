current_balance=10000
print("Welcome to the ATM!")
print("1. Balance Inquiry")
print("2. Withdraw Cash")
print("3. Deposit Cash")
print("4. Exist")
choice =  int(input("Please enter your choice (1-4): "))
if choice == 1:
    print("Your current balance is: {current_balance}")
elif choice == 2:
    amount = int(input("Enter the amount to withdraw: "))
    if amount > current_balance :
        print("Insufficient balance.")
    else:
            current_balance =  current_balance - amount
            print(f"Withdrawl successful! Your new balance is: {current_balance}")
elif choice == 3:
    amount = int(input("Enter the amount to deposit: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
    else:
            current_balance =  current_balance + amount
            print(f"Deposit successfull! Your new balance is: {current_balance}")
elif choice == 4:
    print("Thank you for using the ATM. Goodbye!")
else:
    print("Invalid choice. Please try again.")
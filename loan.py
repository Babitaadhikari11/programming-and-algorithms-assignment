#  a program to check if a user qualifies for a loan:
income = float(input("Enter your  income: "))
credit_score = int(input("Enter your credit score: "))
if income > 50000:
    if credit_score > 700:
        print("Loan is approved")
    elif credit_score <= 700 and credit_score>=600:
        print("Loan approved with a higher interest rate.")
    else:
        print("Loan is rejected due to low credit score.")
else:
    print("Loan rejected due to insufficient income.")

# Ask a user for a username and password. If the username is correct, check if the password is correct, and display appropriate login messages.
username = "admin"
password = "password123"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username =="admin":
    if password == "password123":
        print("Login successful!")
    else:
        print("Incorrect password!")
else:
    print("Incorrect credentials!")

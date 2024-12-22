# Accept input from user and print "fizz buzz", fizz and buzz if divisible by both, divisible by only 3 and only 5 respectively or else print the same value of number
num=int(input("Enter the number: "))
if num%3==0 and num%5==0:
    print("Fizz Buzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(num)
    
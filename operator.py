# a program to accept two numbers and mathematical operators and perform operation accordingly.
num_1=eval(input("Enter a first number: "))
num_2=eval(input("Enter a second number: "))
operation={"+":num_1+num_2,"-":num_1-num_2,"/":num_1/num_2,"*":num_1*num_2}
operator=input("Enter a required operator: ")
if operator in operation:
    print(operation[operator])


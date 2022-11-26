# PROGRAM TO CHECK IF A NUMBER IS IN FIBONACCI SERIES OR NOT

# defining a function to check if the given number is in fibonacci series or not 

def fibonacci(num):
# Taking x=0 and y=1
    x = 0
    y = 1
    if num == 0 or num == 1 :
        return 1
    while y <= num :
        z = x + y
        x = y
        y = z
        if z == num:
            return 1
            break

# taking input from the user

a = 1
while a == 1:
    number = int(input("Enter the number: "))

# Calling the function to check if the given number is in fibonacci series or not

    if fibonacci(number) == 1 :
        print("The given number is in Fibonacci Series: ",number)
    else :
        print("The given number is not in Fibonacci series: ",number)

# Checking if the user wants to check for more number

    x = int(input("Enter 1 if you want to check for more number: "))
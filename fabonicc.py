# Taking Number Input From User
number = int(input("Enter the number: "))

# Defining a Function Name as fibonacci

def fibonacci(num):

# Taking x=0 and y=1
    x = 0
    y = 1
    if num == 0 or num == 1 :
        return 1
# Code for fibonacci series
   
    while y <= num :
        z = x + y
        x = y
        y = z
        if z == num:
            return 1
            break

# Putting condition for checking the given number are in fibonacci series or not

if fibonacci(number) == 1 :
    print("The given number is in Fibonacci Series: ",number)
else :
    print("The given number is not in Fibonacci series: ",number)




x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

try:
    z=x/y
except Exception as ex:
    print("exception occured",ex)
    z=None
print("Division is: ",z)
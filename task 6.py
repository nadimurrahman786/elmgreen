import turtle

# Get an integer
my_num = int(input("Type in an integer"))
my_div = int(input("Type in a divisor"))


# Check divisor not zero
if my_div != 0:
    print (my_num // my_div, "remainder", my_num%my_div)



# Get an integer and a divisor from the user
my_num = int(input("Type in an integer"))
my_div = int(input("Type in a divisor"))


# Check divisor not zero
if my_div != 0:
    # print the integer divison and then the remainder
    print (my_num // my_div, "remainder", my_num%my_div)


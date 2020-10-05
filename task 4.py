# Get an integer from user
my_value = int(input("Type in an option between 1 and 3"))

# Check if it is between 1 and 3
while my_value < 1 or my_value > 3:
    # If not between 1 and 3 then ask again
    my_value = int(input("Type in an option between 1 and 3"))
#end while
print ("Option", my_value, "selected")

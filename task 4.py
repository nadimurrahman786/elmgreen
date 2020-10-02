# Get an integer
my_value = int(input("Type in an option between 1 and 3"))

# Check if 
while my_value < 1 or my_value > 3:
    my_value = int(input("Type in an option between 1 and 3"))
#end while
print ("Option", my_value, "selected")

import turtle

# Get an integer
sides = int(input("Type in the number of sides of your shape"))
length = int(input("Type in the length of the sides"))

# Check if 
counter = 0
while counter < sides:
    turtle.forward(length)
    turtle.right(360/sides)
    counter = counter + 1
# end while


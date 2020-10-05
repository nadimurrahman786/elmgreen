import turtle

# Get an number of sides and length of sides from the user
sides = int(input("Type in the number of sides of your shape"))
length = int(input("Type in the length of the sides"))

# Set counter for loop to zero
counter = 0
# loop round for each side
while counter < sides:
    # move forward length
    turtle.forward(length)
    # Turn the number of degrees
    turtle.right(360/sides)
    # Increase counter
    counter = counter + 1
# end while


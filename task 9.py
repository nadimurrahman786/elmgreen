
from random import randint
# List of options
options = ["R", "P", "S"]

# get word from users
user_str = input ("Get user input")
#user_str = "R"
user = options.index(user_str)

# Generate computer option
computer = randint(0,2)
#computer = 1

if computer == user:
    print ("You:", user_str, "Computer:", options[computer],"Draw")
else:
    # Check winning cominations for computer
    if (user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0):
        print ("You:", user_str, "Computer:", options[computer],"I win")
    else:
        # Otherwise user wins
        print ("You:", user_str, "Computer:", options[computer],"You win")
    # end if
# end if
    




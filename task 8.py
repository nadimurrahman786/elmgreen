
# Get an integer
word = input("Type in a word")

# Initialise variables
new_word = ""

# loop through the word
while len(word) > 0:
    # add last letter to new word
    new_word = new_word + word[-1]
    # shorten the original word by taking off the last letter
    word = word[:-1]
# end while

# output new word
print (new_word)



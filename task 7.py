
# Get an integer from the user
my_num = int(input("Type in an integer"))

# use division to get hundreds
hundreds = my_num //100

# take off hundereds and divide by ten
tens = (my_num - hundreds*100) // 10

# take off hundereds and tens
units = my_num - hundreds * 100 - tens * 10

print (hundreds, "hundreds", tens, "tens", units, "units")


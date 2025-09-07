# Range minimum and maximum bounds
min_number = 0
max_number = 100

# TODO: Enter user input
#number = None  # Enter number
number = float(input("Enter number: "))
if (0 <= number <= 100):
    valid_score = "Yes"
else:
    valid_score = "No"
# TODO: Notify user if the number is a valid score
#valid_score = None
print("Valid score:", valid_score)

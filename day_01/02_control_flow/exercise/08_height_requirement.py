minimum_height = 138

# TODO: Ask the user for the following inputs
user_height = float(input())  # User height (in cm)
if (user_height >= minimum_height):
    can_enter_ride = "Yes"
else:
    can_enter_ride = "No"
# TODO: Notify user if they can enter the ride
#can_enter_ride = None
print("Can enter the ride:", can_enter_ride)

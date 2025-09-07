# Expected password (you can change the value)
correct_password = "pass"

# Enter user password
password_input = input("Please provide password: ")

# TODO: Notify user if password is valid
if (password_input == correct_password):
    correct_password_given = "YES"
else:
    correct_password_given = "No"
#correct_password_given = None
print("Access:", correct_password_given)

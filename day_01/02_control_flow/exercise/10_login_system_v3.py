# Expected password (you can change the value)
correct_password = "pass"

# Enter user password
password_input = input("Please provide password: ")

# TODO: Notify user if password is valid or invalid
#correct_password_given = None
if password_input == correct_password:
    print("Access Granted")
else:
    print("Access Denied")

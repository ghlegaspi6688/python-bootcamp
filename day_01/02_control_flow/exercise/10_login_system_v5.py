# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
if (username_input == correct_username and password_input == correct_password) or (username_input == admin_username and password_input == admin_password):
    print("Access Granted")
else:
    print("Access Denied")
correct_credentials = None
print("Access Granted")
print("Access Denied")

import tkinter

root = tkinter.Tk()


# TODO: Add label for instructions
label = tkinter.Label(
    root,
    text="Enter your Password",
    font=("Arial", 11, "")
)
label.pack()
# TODO: Add entry for instructions
entry = tkinter.Entry(root)
entry.pack()
def show_input(event):
    given_text = entry.get()
    if given_text == "pass":
        label = tkinter.Label(
            root,
            text="Password correct! Access granted.",
            font=("Arial", 11, "bold")
        )
        label.pack()
    else:
        label = tkinter.Label(
            root,
            text="Incorrect password. Try again.",
            font=("Arial", 11, "bold")
        )
    #print(given_text)
root.bind("<Return>", show_input)

label = tkinter.Label(
    root,
    text="Enter your Password and press Enter",
    font=("Arial", 11, "")
)
label.pack()
# TODO: Add StringVar for instruction

# TODO: Add label using StringVar

#user_input = tkinter.StringVar(root, value="Enter your Password and press Enter.")
#entry_bind.py

#label = tkinter.Label(root, textvariable=user_input)
#label.pack()

def check_password(event):
    correct_password = "pass"

    # TODO: Check if entry.get() has correct value


# TODO: Add key bindings for check_password

root.mainloop()

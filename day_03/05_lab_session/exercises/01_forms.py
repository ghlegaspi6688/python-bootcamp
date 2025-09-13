import tkinter
import json
root = tkinter.Tk()

# TODO: Create StringVar for name
name = """
Name: 
"""
name = tkinter.Label(root, text=name)
name.pack()
# TODO: Create StringVar entry for name
outname = tkinter.Entry(root)
outname.pack()
# TODO: Create StringVar for age
age = """
Age: 
"""
age = tkinter.Label(root, text=age)
age.pack()
# TODO: Create StringVar entry for age
outage = tkinter.Entry(root)
outage.pack()

# TODO: Create StringVar for theme
theme = """
Preferred Theme: 
"""
theme = tkinter.Label(root, text=theme)
theme.pack()
# TODO: Create StringVar entry for theme
outtheme = tkinter.StringVar(value="Light")
radio1 = tkinter.Radiobutton(
root, text="Light", variable=outtheme, value="Light")
radio1.pack()
radio2 = tkinter.Radiobutton(
root, text="Dark", variable=outtheme, value="Dark")
radio2.pack()

# TODO: Create BooleanVar for subscribe

# TODO: Create BooleanVar entry for
outsub = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
    root,
    text="Subscribe to newsletter",
    variable=outsub
)
checkbox.pack()

# TODO: Create IntVar for rating
rating = """
Rating: 
"""
rating = tkinter.Label(root, text=rating)
rating.pack()
# TODO: Create IntVar for entry rating
slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(
    root,
    from_=1,
    to=5,
    orient="horizontal",
    variable=slider_value
)
slider.pack()

# TODO: Create function for saving values to JSON
# TODO: Create button for submit + save
def submit():
    data = {
        "Name":   outname.get(),
        "Age":   outage.get(),
        "Theme":   outtheme.get(),
        "Subscribe":   outsub.get(),
        "Rating":   slider.get(),
    }
    with open("data.json", "w") as file:
        json.dump(data, file)
#outsub = tkinter.Button(root, text="Submit", command=show_input)
outsubmit = tkinter.Button(root, text="Submit", command=submit)

outsubmit.pack()


root.mainloop()

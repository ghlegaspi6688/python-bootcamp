import tkinter
root = tkinter.Tk()
label = tkinter.Label(
    root,
    text="Hello",
    font=("Arial", 14, "bold italic"),
    fg="red",
    bg="yellow",
    width=100,
    height=20,
    padx=10,
    pady=200,
    #props.py,
)
label.pack()
root.mainloop()

import tkinter

root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("1200x400")

label = tkinter.Label(root, text="Hello",
#label = tkinter.Label(root, text="Hello", #next line
label.pack()

message = """
    Hello waorl
    Hello again
"""
label = tkinter.Label(root, text=message) #other method multiline
label.pack()

next_label = tkinter.Label(root, text="World")
next_label.pack()

root.mainloop()

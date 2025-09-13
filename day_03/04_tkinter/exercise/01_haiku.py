import tkinter

root = tkinter.Tk()
root.title("Haiku")
root.geometry("1200x400")


message = """
Loops within loops again
A silent function returns
The logic is clear
"""
label = tkinter.Label(root, text=message) #other method multiline
label.pack()
root.mainloop()
# TODO: Show message using a label

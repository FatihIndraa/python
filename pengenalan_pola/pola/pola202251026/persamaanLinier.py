from tkinter import*

root = Tk()
root.geometry("300x300")

OPTIONS = [
    "Option 1",
    "Option 2",
    "Option 3"]#etc

variable = StringVar()
variable.set(OPTIONS[0])#default value

w = OptionMenu(root, variable, *OPTIONS)
w.pack()

root.mainloop()
from tkinter import *
from fungsi import tampilkan_grafik

def pilihan_diubah(*args):
    if variable.get() == "Option 1":
        tampilkan_grafik()

root = Tk()
root.geometry("300x300")

OPTIONS = [
    "Option 1",
    "Option 2",
    "Option 3"]

variable = StringVar()
variable.set(OPTIONS[0])

variable.trace("w", pilihan_diubah)
w = OptionMenu(root, variable, *OPTIONS)
w.pack()

root.mainloop()

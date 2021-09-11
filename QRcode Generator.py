from tkinter import *
import pyqrcode

root = Tk()

root.geometry("400x400+500+200")
root.maxsize(400, 400)
root.minsize(400, 400)
root.title("QR Code Generator")


def create():
    url = pyqrcode.create(text_value_1.get())
    url.png("text_value_2.get()", scale=6)
    entry_1.delete(0, END)
    entry_2.delete(0, END)


lable_1 = Label(root, text="Enter any Text", font="comicsansns 20 bold")
lable_1.pack(pady=20)
text_value_1 = StringVar()
entry_1 = Entry(root, textvariable=text_value_1, font="comicsansns 20 bold", borderwidth=5)
entry_1.pack(pady=20)
lable_2 = Label(root, text="Enter Name of file", font="comicsansns 20 bold")
lable_2.pack(pady=10)
text_value_2 = StringVar()
entry_2 = Entry(root, textvariable=text_value_2, font="comicsansns 20 bold", borderwidth=5)
entry_2.pack(pady=20)

button = Button(root, text="Create", font="comicsansns 15 bold", command=create, borderwidth=5)
button.pack(pady=10)

lable_3 = Label(root, text="Creator: Aditya.R", font="comicsansns 8 bold")
lable_3.pack(anchor="se")

root.mainloop()

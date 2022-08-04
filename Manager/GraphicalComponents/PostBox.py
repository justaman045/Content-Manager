from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText
import pyperclip as clip
import pymsgbox as pg



def PostBox(title):
    root = Tk()
    root.geometry("500x500")
    root.title(title)
    root.resizable(width=False, height=False)
    Pos = StringVar()

    def MoveToNext():
        Post = textbox.get(1.0, "end-1c")
        Pos.set(Post)
        clip.copy(f"{Pos.get()}")
        root.destroy()

    labl = Label(root, text=f"{title} in the below TextBox")
    labl.config(font=("Courier", 12))
    labl.place(x=10, y=20)

    textbox = ScrolledText(root, height=22, width=58)
    textbox.place(x=8, y=60)

    btn3 = Button(root, text="Next", command=MoveToNext)
    btn3.place(x=225, y=430)

    root.mainloop()
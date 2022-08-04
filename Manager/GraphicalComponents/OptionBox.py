import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText
import pyperclip as clip
import pymsgbox as pg
import requests
from dotenv import load_dotenv

load_dotenv()


def PlatformsToUpload(platforms=['Dev.to', 'Medium', "CodeItDown", "All"], title="Select the Platforms to Upload"):
    root = Tk()
    root.geometry("500x500")
    root.title(title)
    root.resizable(width=False, height=False)

    def MoveToNext():
        AllPlatformsSelected = ""
        for key, value in optionCheckBox.items():
            val = value.get()
            if val != 0:
                AllPlatformsSelected += f"{key}+"
        clip.copy(AllPlatformsSelected)
        root.destroy()

    InstalledApps = platforms

    optionCheckBox = {}

    if len(InstalledApps) == 0:
        pg.alert(
            "No Videos/Blog Posts to Promote", os.getenv("BotName"))
        exit()
    else:
        for i in InstalledApps:
            optionCheckBox[f"{i}"] = IntVar()

    labl = Label(root, text=f"Select the Platforms to Upload")
    labl.config(font=("Courier", 12))
    labl.place(x=80, y=20)

    text = ScrolledText(root, width=60, height=15)
    text.place(x=8, y=60)
    for key, value in optionCheckBox.items():
        text.window_create('end', window=Checkbutton(text=key, variable=value))

    btn = Button(root, text="Post", command=MoveToNext)
    btn.place(x=225, y=325)

    root.mainloop()

def getAllCateogarys():
    allCateogary = requests.get(f'{os.getenv("codeitdownDomain")}/allCateogary/').json()
    licat = [x["Cateogary"] for x in allCateogary]
    PlatformsToUpload(platforms=licat, title="Select The Cateogary's in which Blogs to be Uploaded")

def getAllHashtags():
    allCateogary = requests.get(
        f'{os.getenv("codeitdownDomain")}/hashtagall/').json()
    licat = [x["Hashtag"] for x in allCateogary]
    PlatformsToUpload(platforms=licat, title="Select The Cateogary's in which Blogs to be Uploaded")
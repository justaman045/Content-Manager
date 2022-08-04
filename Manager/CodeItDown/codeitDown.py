import os
import requests
from Manager.GraphicalComponents.PostBox import PostBox
import pyperclip as clip
import pymsgbox as pg



def CodeItDown():
    url = f'{os.getenv("BlogDomain")}/mail/'

    MailHead = pg.prompt("Enter the Mail Title", os.getenv("BotName"))
    PostBox('Enter your Mail in Markdown')

    payload = {'BlogName': MailHead,
            'content': clip.paste()}
    files = [

    ]
    headers = {}

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    print(response.text)

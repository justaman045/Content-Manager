import json
import os
import requests
import pyperclip as clip
import pymsgbox as pg

from Manager.GraphicalComponents.PostBox import PostBox
from dotenv import load_dotenv

load_dotenv()

def ProjektNotify():
    url = f"{os.getenv('projektnotify')}/mail/"

    MailHead = pg.prompt("Enter the Mail Title", os.getenv('BotName'))
    PostBox('Enter your Mail in Markdown')

    payload = {'headline': MailHead,
            'mail': clip.paste()}
    files = [

    ]
    headers = {}

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    print(response.text)

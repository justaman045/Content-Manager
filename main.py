import os
import pymsgbox as pg
from Manager.GraphicalComponents.OptionBox import PlatformsToUpload
from Manager.ProjektNotify.ProjektNotify import ProjektNotify
from Manager.CodeItDown.codeitDown import CodeItDown
from Manager.AutoBlogPost.main import AutoBlogPost
from Nessesary_Components.ScriptUpdate import GetUpdate
from Nessesary_Components.rss_json import get_posts_details
import pyperclip as clip
from dotenv import load_dotenv

load_dotenv()

try:
    GetUpdate()
except:
    pass

option = pg.confirm("Select your option to Manage", os.getenv("BotName"), buttons=['Mail', 'Promote Post', "Blog Post"])

if option == 'Mail':
    mailOption = pg.confirm('Whome to Mail??', os.getenv("BotName"), buttons=['Code it Down Subscribers', 'Projekt Notify Subscribers'])
    if mailOption == 'Code it Down Subscribers':
        CodeItDown()
    elif mailOption == 'Projekt Notify Subscribers':
        ProjektNotify()
    else:
        exit()
elif option == 'Promote Post':
    platform = pg.confirm("From which Platform you want to Promote your Post", os.getenv("BotName"), buttons=['CodeitDown', "HashNode", "Dev.to", "Medium", "YouTube", "Twitch"])
    data = get_posts_details(os.getenv(str(platform)))
    Headline = []
    for i in data['posts']:
        Headline.append(i['title'])
    PlatformsToUpload(platforms=Headline, title='Select any One to Promote over all your Socials Connected')
    if len(str(clip.paste())[:-1].split('+')) >= 2:
        pg.alert("Taking the Latest Headline to Promote as Promotion can be only Occured for 1 Only")
elif option == 'Blog Post':
    AutoBlogPost()
else:
    exit()

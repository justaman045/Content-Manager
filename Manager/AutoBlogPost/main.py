import os
import sys
import pymsgbox as pg
from Manager.AutoBlogPost.poster import PostToDev, PostToMedium, PostToCodeItDown
from Manager.GraphicalComponents.OptionBox import PlatformsToUpload, getAllCateogarys, getAllHashtags
import pyperclip

from Manager.GraphicalComponents.PostBox import PostBox
from dotenv import load_dotenv

from Nessesary_Components.isImageOrNot import is_url_image

load_dotenv()


def AutoBlogPost():
    title = pg.prompt("Enter the Title for the Blog", os.getenv("BotName"))
    if title == None:
        sys.exit()
    elif len(title) <= 5:
        sys.exit()
    slug = str(title).replace(" ","-")
    image = pg.prompt("Enter the URL of Image for the Blog", os.getenv("BotName"))
    if is_url_image(image) == False:
        sys.exit()
    getAllHashtags()
    tags = str(pyperclip.paste()).replace("#", ",").replace(" ", ",").replace("+",",").split(",")[:4]
    PostBox(title="Write the Blog")
    content = str(pyperclip.paste()).replace("```", "`")
    if len(content) <= 25:
        pg.alert("Blog Post Length doesn't comply with the Blog Post Providers", os.getenv("BotName"))
    PlatformsToUpload()
    Platforms = str(pyperclip.paste()).split("+")
    if len(Platforms) == 0:
        sys.exit()
    for i in Platforms:
        if i == "Dev.to":
            PostToDev(title, content, tags, image=image, canonicalURL=f'{os.getenv("BlogDomainPostURL")}{slug}')
        elif i == "Medium":
            PostToMedium(title, content, tags, image=image,
                         canonicalURL=f'{os.getenv("BlogDomainPostURL")}{slug}')
        elif i == "CodeItDown":
            getAllCateogarys()
            PostToCodeItDown(title, content, tags, pyperclip.paste())
        elif i == "All":
            getAllCateogarys()
            PostToCodeItDown(title, content, tags, pyperclip.paste())
    

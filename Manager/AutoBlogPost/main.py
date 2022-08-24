# Import all the nessesary Modules 
import os
import sys
import pymsgbox as pg
from Manager.AutoBlogPost.poster import PostToAll, PostToDev, PostToMedium, PostToCodeItDown
from Manager.GraphicalComponents.OptionBox import PlatformsToUpload, getAllCateogarys, getAllHashtags
import pyperclip
from Manager.GraphicalComponents.PostBox import PostBox
from dotenv import load_dotenv
from Nessesary_Components.isImageOrNot import is_url_image

# Load the Environment Variables written in .env file
load_dotenv()

# Get the Data to Post on Blogging Platforms 
def AutoBlogPost():

    # Get the Title of the Blog Post and check if nothing entered then quit
    title = pg.prompt("Enter the Title for the Blog", os.getenv("BotName"))
    if title == None:
        sys.exit()
    elif len(title) <= 5:
        sys.exit()

    # Generate a Slug for the Blog Post 
    slug = str(title).replace(" ","-")

    # Get the Cover Image to be Uploaded and check if nothing entered then quit
    image = pg.prompt("Enter the URL of Image for the Blog", os.getenv("BotName"))
    if is_url_image(image) == False:
        sys.exit()

    # Get all the Hashtags ( Currently it will be according to my Blogging website )
    # To add more change the API to maybe Dev.to Hashtags it has a wide range of hashtags for Developers 
    getAllHashtags()
    tags = str(pyperclip.paste()).replace("#", ",").replace(" ", ",").replace("+",",").split(",")[:4]

    # Get the Blog Post in Markdown Format with a Length of more than 25 Charecters 
    PostBox(title="Write the Blog")
    content = str(pyperclip.paste()).replace("```", "`")
    if len(content) <= 25:
        pg.alert("Blog Post Length doesn't comply with the Blog Post Providers", os.getenv("BotName"))

    # Get on which Platform to Upload either it is Dev.to, Medium or Personal Bloggin Website 
    PlatformsToUpload()
    Platforms = str(pyperclip.paste()).split("+")
    if len(Platforms) == 0:
        sys.exit()

    # Now check which is selected then Upload to particular Platform 
    for i in Platforms:
        if i == "Dev.to":
            PostToDev(title, content, tags, image=image, canonicalURL=f'{os.getenv("BlogDomainPostURL")}{slug}')
        elif i == "Medium":
            PostToMedium(title, content, tags, image=image,
                         canonicalURL=f'{os.getenv("BlogDomainPostURL")}{slug}')
        elif i == "CodeItDown":
            getAllCateogarys()
            PostToCodeItDown(title, content, tags, pyperclip.paste(), image)
        elif i == "All":
            getAllCateogarys()
            PostToAll(title, content, tags, pyperclip.paste(), image)
            pg.alert("Uploaded Blog Posts")

    

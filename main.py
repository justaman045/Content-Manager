# Import all the nessesary Modules 
import os
import sys
import pymsgbox as pg
from Manager.ProjektNotify.ProjektNotify import ProjektNotify
from Manager.CodeItDown.codeitDown import CodeItDown
from Manager.AutoBlogPost.main import AutoBlogPost
from Nessesary_Components.Promote import Promote
from Nessesary_Components.ScriptUpdate import GetUpdate
from dotenv import load_dotenv

# Load the Environment Variables written in .env file 
load_dotenv()

# Check for Update then notify the User 
# GetUpdate()

# What the user wants to do 
option = pg.confirm("Select your option to Manage", os.getenv("BotName"), buttons=['Mail', 'Promote Post', "Blog Post"])

# If It's mail then send the mail 
if option == 'Mail':

    # To whome the user wants to send mail either it is Blog Subscribers or the waiting List Subscribers 
    mailOption = pg.confirm('Whome to Mail??', os.getenv("BotName"), buttons=['Code it Down Subscribers', 'Projekt Notify Subscribers'])
    
    # If Blog Subscribers then send mail to them 
    if mailOption == 'Code it Down Subscribers':
        CodeItDown()

    # else if to Product Waiting List Subscribers 
    elif mailOption == 'Projekt Notify Subscribers':
        ProjektNotify()

    # If no one then Quit 
    else:
        sys.exit()

# If the User Wants to Promote the Blog Post/Videos 
elif option == 'Promote Post':

    # Choose what to Promote from either it is from Medium, YouTube or what??
    platform = pg.confirm("From which Platform you want to Promote your Post", os.getenv("BotName"), buttons=['CodeitDown', "HashNode", "Dev.to", "Medium", "YouTube", "Twitch"])

    # Now Promote it 
    Promote(platform)

# If User wants to Write a Blog Post then Call it's respective function 
elif option == 'Blog Post':
    AutoBlogPost()

# If Nothing then Quit 
else:
    sys.exit()

import os
import sys
from Nessesary_Components.rss_json import get_posts_details
from Manager.GraphicalComponents.OptionBox import PlatformsToUpload
import pyperclip as clip
import pymsgbox as pg
import tweepy
import praw


def Promote(platform):
    data = get_posts_details(os.getenv(str(platform)))
    Headline, Links, LinksToUpload = [], [], []
    for i in data['posts']:
        Links.append(i['link'])
        Headline.append(i['title'])
    PlatformsToUpload(
        platforms=Headline, title='Select any One to Promote over all your Socials Connected')
    selectedOptions = str(clip.paste()).split("+")[:-1]
    htmlLinks, htmlTitles = '', ""
    for i in range(0, len(selectedOptions)):
        LinksToUpload.append(Links[Headline.index(selectedOptions[i])])
        htmlTitles += f"{i+1}. {selectedOptions[i]}\n"
        htmlLinks += f"{i+1}. {LinksToUpload[i]}\n"
    PlatformsToUpload(platforms=["Twitter", "Reddit"],
                      title='Select Your Socials to Upload to')
    platforms = str(clip.paste()).split("+")[:-1]
    tempMessage = f"Hii, Just so you get to know\n\nI wrote these Blog Posts Named\n{htmlTitles}\n\n You can access the same from the links below \n{htmlLinks}"
    if len(tempMessage) > 280:
        pg.alert(
            f"Your Promotion Message Exceds the Message Length Reduce the Number of Links to Promote.\n\nThe length of this Message would be {len(tempMessage)}\n\nThis Program will now Quit Please Try again", os.getenv("BotName"))
        sys.exit()
    if platform in ["YouTube", "Twitch"]:
        if len(LinksToUpload) == 1:
            message = f"Hii, Just so you get to know\n\nI made this Video Named\n\n{htmlTitles}\n\n You can access the same from the links below \n\n{htmlLinks[3:]}"
        else:
            message = f"Hii, Just so you get to know\n\nI made these Videos Named\n\n{htmlTitles}\n\n You can access the same from the links below \n\n{htmlLinks}"
    else:
        if len(LinksToUpload) == 1:
            message = f"Hii, Just so you get to know\n\nI wrote this Blog Post Named\n\n{htmlTitles}\n\n You can access the same from the links below \n\n{htmlLinks[3:]}"
        else:
            message = f"Hii, Just so you get to know\n\nI wrote these Blog Posts Named\n\n{htmlTitles}\n\n You can access the same from the links below \n\n{htmlLinks}"
    for i in platforms:
        if i == "Twitter":
            if len(message) < 270:
                newMessage = f'{message}\n#DEVCommunity'
            elif len(message) < 260:
                newMessage = f'{message}\n#100DaysOfCode'
            elif len(message) < 250:
                newMessage = f'{message}\n#100DaysOfCode #python'
            elif len(message) < 240:
                newMessage = f'{message}\n#100DaysOfCode #python #DEVCommunity '
            else:
                newMessage = message
            auth = tweepy.OAuthHandler(
                os.getenv("ConsumerKeyTwitter"), os.getenv("ConsumerKeySecretTwitter"))
            auth.set_access_token(
                os.getenv("AccesTokenTwitter"), os.getenv("AccessTokenSecretTwitter"))

            api = tweepy.API(auth)
            client = tweepy.Client(consumer_key=os.getenv("ConsumerKeyTwitter"), consumer_secret=os.getenv("ConsumerKeySecretTwitter"),
                                   access_token=os.getenv("AccesTokenTwitter"), access_token_secret=os.getenv("AccessTokenSecretTwitter"), bearer_token=os.getenv("BearerTokenTwitter"))
            client.create_tweet(text=newMessage)
        if i == "Reddit":
            subreddits = ["programming", "ProgrammerHumor",
                          "learnprogramming", "AskProgramming", "coding", "learnpython"]
            pg.alert("Subreddits not confirmed yet as so this feature of reddit promotion\n\nAs a result this program will skip this promotion", "In Development")

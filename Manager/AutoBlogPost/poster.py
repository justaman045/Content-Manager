import os
import requests
import json
from dotenv import load_dotenv
import pymsgbox as pg

load_dotenv()


# Dev.to Post Request
def PostToDev(title: str, content: str, tags: list, image: str, canonicalURL: str):
    headers = {
        'Content-Type': 'application/json',
        'api-key': os.getenv("devAPI"),
    }


    body = json.dumps({
        "article": {
            "title": title,
            "published": False,
            "body_markdown": content,
            "main_image": image,
            "canonical_url": canonicalURL,
            "tags": tags,
        }
    })

    respone = requests.post('https://dev.to/api/articles', headers=headers, data=body)
    if respone.status_code == 201:
        pg.alert("Blog Post Sucessfully Uploaded on Dev.to", os.getenv("BotName"))
    else:
        pg.alert("Error Posting on Dev.to.\n\nCheck Terminal for Errors", os.getenv("BotName"))


# Medium Post Request
def PostToMedium(title: str, content: str, tags: list, image: str, canonicalURL: str):
    MediumAPIUrl = 'https://api.medium.com/v1/'
    headers = {
        'Authorization': "Bearer " + os.getenv("mediumAPI"),
        'Content-Type': 'application/json',
    }
    meRequest = requests.get(f'{MediumAPIUrl}me', headers=headers).json()
    userURL = f'{MediumAPIUrl}users/{meRequest["data"]["id"]}/posts'
    slug = str(title).replace(" ", "-")
    content = f'<img src="{image}" alt="{slug}"> {content}'
    body = json.dumps({
        'title': title,
        'contentFormat': 'markdown',
        'tags': tags,
        "canonicalUrl": canonicalURL,
        "notifyFollowers": False,
        'publishStatus': 'draft',
        'content': content,
    })
    Publications = requests.post(userURL, headers=headers, data=body)
    if Publications.status_code == 201:
        pg.alert("Blog Post Sucessfully Uploaded on Medium",
                 os.getenv("BotName"))
    else:
        pg.alert("Error Posting on Medium.\n\nCheck Terminal for Errors",
                 os.getenv("BotName"))


def PostToCodeItDown(title: str, content: str, tags: list, cateogary: str, image: str):
    tempTags =  ""
    for tag in tags:
        tempTags+=f'{tag} '
    tags = str(tempTags).replace("#", ",").replace(" ", ",").replace("+",",")
    cateogary = str(cateogary).replace("#", ",").replace(" ", ",").replace("+", ",").split(",")[:1]
    payload = {
        'hashtag': tag,
        'BlogName': title,
        'content': content,
        'cat': cateogary,
        "image": image
        }

    response = requests.get(f'{os.getenv("codeitdownDomain")}/upload/', data=payload)

def PostToAll(title: str, content: str, tags: list, cateogary: str, image: str):
    tempTags =  ""
    for tag in tags:
        tempTags+=f'{tag} '
    tags = str(tempTags).replace("#", ",").replace(" ", ",").replace("+", ",")
    cateogary = str(cateogary).replace("#", ",").replace(" ", ",").replace("+", ",").split(",")[:1]
    payload = {
        'hashtag': tag,
        'BlogName': title,
        'content': content,
        'cat': cateogary,
        "image": image
    }

    response = requests.get(f'{os.getenv("codeitdownDomain")}/uploadToAll/', data=payload)


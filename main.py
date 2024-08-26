import requests


def get_description(url):
    response = requests.get(url)
    content = response.json()
    description = content["explanation"]
    return description


def get_picture(url):
    response = requests.get(url)
    content = response.json()
    pic_url = content["hdurl"]
    pic_response = requests.get(pic_url)
    with open("image.jpg", "wb") as file:
        file.write(pic_response.content)


def get_title(url):
    response = requests.get(url)
    content = response.json()
    t = content["title"]
    return t



#!/usr/bin/env python3.7

"""
    Python script to automatically change the background
    for gnome based window managers.

    Images are fetched from unsplash via this library:
    https://github.com/yakupadakli/python-unsplash
"""

import json
import os
import subprocess
import urllib.request

from unsplash.api import Api
from unsplash.auth import Auth


def load_credentials(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)


def download_image(api, url):
    file_name = "image.jpg"
    urllib.request.urlretrieve(url, file_name)
    return file_name


def set_image_as_wallpaper(file_name):
    working_directory = os.path.dirname(os.path.abspath(__file__))
    subprocess.run(f"gsettings set org.gnome.desktop.background picture-uri file:///{working_directory}/{file_name}".split(" "))
    print("Wallpaper changed!")


def main():
    data = load_credentials('credentials.json')

    client_id = data['client_id']
    client_secret = data['client_secret']
    redirect_uri = data['redirect_uri']

    auth = Auth(client_id, client_secret, redirect_uri)
    api = Api(auth)

    query = "landscape"
    orientation = "landscape"
    images = api.photo.random(query=query, orientation=orientation)

    file_name = download_image(api, images[0].links.download)
    set_image_as_wallpaper(file_name)


if __name__ == '__main__':
    main()

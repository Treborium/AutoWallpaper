#!/usr/bin/env python3.7

"""
    automatically change the background for gnome based window managers.
"""

import json
import os
import subprocess
import urllib.request

URL = "https://source.unsplash.com/featured/2556x1600?landscape"


def download_image(url):
    file_name = "image.jpg"
    urllib.request.urlretrieve(url, file_name)
    return file_name


def set_image_as_wallpaper(file_name):
    working_directory = os.path.dirname(os.path.abspath(__file__))
    subprocess.run(f"gsettings set org.gnome.desktop.background picture-uri file:///{working_directory}/{file_name}".split(" "))
    print("Wallpaper changed!")


def main():
    file_name = download_image(URL)
    set_image_as_wallpaper(file_name)


if __name__ == '__main__':
    main()

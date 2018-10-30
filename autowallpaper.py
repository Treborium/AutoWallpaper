#!/usr/bin/env python3.7

"""
    automatically change the background for gnome based window managers.
"""

import os
import subprocess
import urllib.request

URL = "https://source.unsplash.com/featured/2556x1600?landscape"
WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def download_image(url):
    file_name = "image.jpg"
    urllib.request.urlretrieve(url, WORKING_DIRECTORY + "/" + file_name)
    return file_name


def set_image_as_wallpaper(file_name):
    subprocess.run(f"gsettings set org.gnome.desktop.background picture-uri file:///{WORKING_DIRECTORY}/{file_name}".split(" "))
    print("Wallpaper changed!")


def main():
    file_name = download_image(URL)
    set_image_as_wallpaper(file_name)


if __name__ == '__main__':
    main()

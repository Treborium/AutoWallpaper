#!/usr/bin/env python3.7

"""
    automatically change the background for gnome based window managers.
"""

import os
import subprocess
import sys
import urllib.request

URL = "https://source.unsplash.com/featured/2556x1600"
WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def download_image(url, query_params):
    file_name = "image.jpg"
    urllib.request.urlretrieve(
        f"{url}?{query_params}", WORKING_DIRECTORY + "/" + file_name)
    return file_name


def set_image_as_wallpaper(file_name):
    subprocess.run(
        f"gsettings set org.gnome.desktop.background picture-uri file:///{WORKING_DIRECTORY}/{file_name}".split(" "))
    print("Wallpaper changed!")


def main(args):
    file_name = download_image(URL, query_params)
    set_image_as_wallpaper(file_name)


if __name__ == '__main__':
    query_params = "landscape"
    if len(sys.argv) > 1:
        query_params = sys.argv[1]
    main(query_params)

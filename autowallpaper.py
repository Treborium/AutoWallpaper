#!/usr/bin/env python3

from unsplash.api import Api
from unsplash.auth import Auth

client_id = "af34b34a50e5c593fbefa367960d3e05220cecd4e66ca2f819183ab85721b931"
client_secret = "4ee99d15dda3e265c678e4adf99a82316225e725fe0e0cd040118608717d0bb0"
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"

auth = Auth(client_id, client_secret, redirect_uri)
api = Api(auth)

response = api.photo.random()
print(response)

# working_directory = os.path.dirname(os.path.abspath(__file__))
# subprocess.run(f"gsettings set org.gnome.desktop.background picture-uri file:///{working_directory}/image.jpg".split(" "))

print("Wallpaper changed!")

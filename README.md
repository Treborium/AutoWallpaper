# Auto Wallpaper


<p align="center">
  <img src="https://source.unsplash.com/featured/720x480?landscape">
</p>

Auto wallpaper is a little python script that fetches and applies a new random wallpaper from unsplash.

## Usage
Simply set up a [cronjob](https://linuxconfig.org/linux-crontab-reference-guide) to execute the script in a custom interval:
```
crontab -e
```

And then add something like this to execute the job once a day at 1 p.m.: 
```
0 13 * * * python3 /path/to/autowallpaper.py
```

You can also just call the script from the console:
```
python3 /path/to/autowallpaper.py
```

You can specify the image category by passing a comma separated list as an argument to the script:
```
python3 /path/to/autowallpaper.py "landscape,winter,night"
``` 
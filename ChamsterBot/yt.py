import os
from os import system, name 
from time import sleep
from pytube import YouTube

link = input("Enter the link of YouTube video:  ")
yt = YouTube(link)
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
musicvideo = input("Do you want music or video?(m/v)    ")
if musicvideo == "v":
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download("./YouTubeDownloadedFilms")
    print("Download completed!!")
    print("You can find your file in program files")
    os.system("main.py")
if musicvideo == "m":
    stream = yt.streams.filter(only_audio=True).first()
    print("Downloading...")
    stream.download("./YouTubeDownloadedMusic")
    print("Download completed!!")
    print("You can find your file in program files")
    os.system("main.py")
# https://www.youtube.com/watch?v=PayvWj2piKg
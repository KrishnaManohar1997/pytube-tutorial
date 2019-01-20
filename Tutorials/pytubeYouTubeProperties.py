# -*- coding: utf-8 -*-
"""
Pytube Properties Usage
"""

# Importing YouTube Module from pytube library
from pytube import YouTube

# Prompting user for Youtube Video link
youtube_url = input("Please enter youtube link ")

# Creating YouTube object with the link
myVideo = YouTube(youtube_url)

# Title of the Video
print("Title : " + myVideo.title)

# Length of the Video in Seconds
print("Duration : " + myVideo.length)

# URL of the Thumbnail of the video
print("Thumbnail Link : " + myVideo.thumbnail_url)

# Description of the Video
print("Description : " + myVideo.description)

# Total Views of the Video
print("Views : " + myVideo.views)

# Age Restricted Content
print("Age Restricted : " + str(myVideo.age_restricted))

# ID of the Video
print("Video ID : " + myVideo.video_id)
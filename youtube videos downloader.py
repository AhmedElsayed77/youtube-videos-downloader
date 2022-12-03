#Notice : You must downlaod Pytube library by commands in cmd : pip install git+https://github.com/pytube/pytube

# For Downloading a Video:

from pytube import YouTube
link_url = input("Enter the video url")
link = link_url # put your video link here
video =YouTube(link)

def finish():
    print ("Download Done") #Confirmation that the video downloaded

 #for hight resolution and output_path for the folder you need the video to be in 
output_path_url = input("Enter the video path") #C:/Users/Kimo Store/Documents/learn
video.streams.get_highest_resolution().download(output_path= output_path_url)

video.register_on_complete_callback(finish()) #calling the confrimation function
 

# For Downloading a playlist:

from pytube import Playlist

Playlist_link =input("Enter the playlist url") # the playlist link
Playlist = Playlist(Playlist_link)
Playlist_path = input("Enter the playlist path")
for video in Playlist.videos:
    video.streams.get_highest_resolution().download(output_path=Playlist_path)
#or
  # video.streams.get_lowest_resolution().download(output_path="  ") for low resolution



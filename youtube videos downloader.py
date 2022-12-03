# For Downloading a Viedo:

from pytube import YouTube
link = "the viedo link" # put your video link here
video =YouTube(link)

def finish():
    print ("Download Done") #Confirmation that the video downloaded

 #for hight resolution and output_path for the folder you need the video to be in 
video.streams.get_highest_resolution().download(output_path="C:/Users/Kimo Store/Documents/learn")

video.register_on_complete_callback(finish()) #calling the confrimation function


# For Downloading a playlist:

from pytube import Playlist
Playlist_link = " " # the playlist link
Playlist = Playlist(Playlist_link)
for video in Playlist.videos:
    video.streams.get_highest_resolution().download(output_path=" the playlist link")
#or
  # video.streams.get_lowest_resolution().download(output_path="  ") for low resolution



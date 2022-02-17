from pytube import YouTube
import ssl
import sys

ssl._create_default_https_context = ssl._create_stdlib_context
link = sys.argv[1]
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download("~/Downloads")
print("Video downloaded")
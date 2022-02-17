<h1>Usage</h1>

  Strat by copying the URL for the video you want to download, then run the following command:

  ```console
  user@python:~$ python youtube.py "URL"
  ```
  replace the "URL" with the actual url
  
  
  
  
  
  ~/Downloads is where you want to save the video:
  ```console
  ...
  stream.download("~/Downloads")
  ...
  ```
  
  you can save the audio only by replacing:
 ```console
  ...
stream = video.streams.get_highest_resolution()
  ...
  ```
  with: 
   ```console
  ...
stream = video.streams.get_audio_only()
  ...
  ```
  
  
  
  
  
  
  you can make an alias to make it a simple porcedure for next times as well

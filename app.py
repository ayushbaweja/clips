import math
import os
from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=iDulhoQ2pro&list=WL&index=1")
title = yt.title
title = title.replace(" ", "\ ")
print(title)
videoLength = int(yt.length / 60)
# stream = yt.streams.filter(progressive=True, res="720p").first()
# stream.download()

splitLength = 10
for i in range(math.ceil(videoLength/splitLength)):
    start =i*60
    length=splitLength*60 
    os.system("ffmpeg -i " + str(title) + ".mp4" + " -ss " + str(start) + " -t " + str(length) + " clip"+str(i)+".mp4")
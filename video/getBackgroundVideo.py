import os
import random
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.Crop import Crop
fileDir = os.path.dirname(os.path.abspath(__file__))

# in the future do automatic scan of background footage folder

videos = {
    "worker":1
}

def getBackgroundVideo(type="worker"):
    videoName = type
    if type == "worker":
        videoName += str(random.randint(0,videos['worker']-1))
    video = VideoFileClip(os.path.join(fileDir,f"background_footage/{videoName}.mp4")).without_audio()
    start_time = random.randint(15, video.duration - 60)
    clip = video.subclipped(start_time, start_time + 60)

    w, h = clip.size
    new_w = int(h * (9 / 16)) // 2 * 2  # Makes sure width is even

    clip = Crop(x_center=w / 2, width=new_w, height=h).apply(clip)
    # clip.write_videofile(os.path.join(fileDir, "../output/asd.mp4"), codec="libx264", fps=30,logger=None)
    # clip = clip.resize(height=1920)
    # clip = clip.crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)

    return clip
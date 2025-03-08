import os
import random
import uuid

from colorama import Fore
from moviepy import VideoFileClip, ImageClip, AudioFileClip, CompositeAudioClip, CompositeVideoClip
from moviepy.video.fx import MultiplySpeed

from video.getBackgroundVideo import getBackgroundVideo
from video.getSubtitles import getSubtitles
from video.getTTS import getTTS

fileDir = os.path.dirname(os.path.abspath(__file__))
# import imageio_ffmpeg
# imageio_ffmpeg.loglevel = "error"  # or "quiet"


def adjust_subtitle_timings(subtitles, original_duration):
    """Adjust subtitle timings based on speed-up factor."""
    speed_factor = original_duration / 60  # e.g., 120 / 60 = 2
    adjusted_subtitles = []

    for subtitle in subtitles:
        # Assuming subtitle is a TextClip with start and duration properties
        new_start = subtitle.start / speed_factor
        new_duration = subtitle.duration / speed_factor
        adjusted_subtitle = subtitle.with_start(new_start).with_duration(new_duration)
        adjusted_subtitles.append(adjusted_subtitle)

    return adjusted_subtitles

def compileVideo(title,bestReply):
    print(Fore.GREEN + "Obtaining Background Video")
    bg_video = getBackgroundVideo()
    print(Fore.GREEN + "Adding Initial Title Screenshot")
    image = ImageClip(os.path.join(fileDir, "../screenshot/reddit_screenshot.png")).with_duration(bg_video.duration)
    image = image.with_duration(4).with_position("center")  # Adjust position if needed

    print(Fore.GREEN + "Generating TTS")
    getTTS(title,bestReply)
    main_audio = AudioFileClip(os.path.join(fileDir, "./tts.mp3"))
    original_duration = main_audio.duration
    main_audio = MultiplySpeed(final_duration=60).apply(main_audio)
    # main_audio.write_audiofile(os.path.join(fileDir, "./tts.mp3"))
    print(Fore.GREEN + "Adding Background Music")
    bg_audio_dir = os.path.join(fileDir, "./background_audio")
    bg_audio_file = random.choice([f for f in os.listdir(bg_audio_dir) if f.endswith(".mp3")])
    bg_audio_path = os.path.join(bg_audio_dir, bg_audio_file)
    bg_audio = AudioFileClip(bg_audio_path).with_duration(bg_video.duration).with_volume_scaled(0.07)
    # print(bg_audio_path)
    # print(bg_audio.duration)
    # start_time = random.randint(15, bg_audio.duration - 60)
    # bg_audio = bg_audio.subclipped(start_time, start_time + 60)


    final_audio = CompositeAudioClip([main_audio, bg_audio.with_start(0)])
    print(Fore.GREEN + "Adding Subtitles")
    subtitles = getSubtitles()

    adjusted_subtitles = adjust_subtitle_timings(subtitles, original_duration)
    # adjusted_base = adjust_subtitle_timings(base, original_duration)
    print(Fore.GREEN + "Assembling Video")
    final_video = CompositeVideoClip([bg_video] + adjusted_subtitles + [image])

    final_video = final_video.with_audio(final_audio)

    random_uuid = uuid.uuid4()
    fileName = f"{str(random_uuid)}.mp4"
    print(Fore.RED + f"Saving Video As {fileName}")
    final_video.write_videofile(os.path.join(fileDir, f"../output/{fileName}"), codec="libx264", fps=30,logger='bar')

    return
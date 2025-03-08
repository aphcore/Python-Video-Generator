import os

import whisper
from moviepy import TextClip, CompositeVideoClip

model = whisper.load_model("small")
fileDir = os.path.dirname(os.path.abspath(__file__))
threshold = 0.15
def generateSubtitles():
    model = whisper.load_model("small")
    result = model.transcribe(os.path.join(fileDir, "./tts.mp3"), word_timestamps=True)

    # Collect all words from all segments into a single list
    all_words = [word for segment in result["segments"] for word in segment["words"]]

    # Handle empty input
    if not all_words:
        return []

    # Initialize subtitle list and the first subtitle
    subtitles = []
    current_subtitle = [all_words[0]]
    current_start = float(all_words[0]['start'])  # Convert np.float64 to float
    current_end = float(all_words[0]['end'])

    # Process each word after the first
    prevHasPunctuation = False
    for word in all_words[1:]:
        gap = float(word['end']) - float(word['start'])

        if (gap < threshold or "%" in word['word']) and not prevHasPunctuation:
            current_subtitle.append(word)
            current_end = float(word['end'])
        else:

            text = ' '.join([w['word'].strip() for w in current_subtitle])
            subtitles.append({'text': text, 'start': current_start, 'end': current_end})
            current_subtitle = [word]
            current_start = float(word['start'])
            current_end = float(word['end'])
        if "." in word['word'] or \
                "," in word['word'] or \
                "?" in word['word']:
            prevHasPunctuation = True
        else:
            prevHasPunctuation = False

    # Append the last subtitle
    text = ' '.join([w['word'].strip() for w in current_subtitle])
    subtitles.append({'text': text, 'start': current_start, 'end': current_end})

    return subtitles
font_path = os.path.join(fileDir, "font/LilitaOne-Regular.otf")

def getSubtitles():
    subtitles = generateSubtitles()
    clips = []


    for sub in subtitles:
        txt_clip = TextClip(
            font_path,
            text=sub['text'],
            font_size=60,
            # font=font_path,
            color='white',
            stroke_color='black',
            stroke_width=16,
            size=(600, 400),
            # method='caption'
        ).with_position(('center')).with_duration(sub['end'] - sub['start']).with_start(sub['start'])
        # stroke_clip = TextClip(
        #     font_path,
        #     text=sub['text'],
        #     font_size=60,
        #     # color='black',  # No fill, just stroke
        #     transparent=True,
        #     stroke_color='black',
        #     stroke_width=10,  # Your large stroke,
        #     size=(600, 600)
        # ).with_position('center').with_duration(sub['end'] - sub['start']).with_start(sub['start'])
        # txt_clip = CompositeVideoClip([fill_clip, stroke_clip])
        clips.append(txt_clip)
    return clips
import whisper

model = whisper.load_model("small")
result = model.transcribe("../video/tts.mp3",word_timestamps=True)
short_subs = []


def combine_subtitles(result, threshold=0.15):

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
print(combine_subtitles(result))
print("           ".join(word['text'] for word in combine_subtitles(result)))

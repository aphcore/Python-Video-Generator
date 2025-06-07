import os
import time

from pyt2s.services import stream_elements
from dotenv import load_dotenv
load_dotenv()
# en_US_Wavenet_D - male
# en_US_Standard_C - female
fileDir = os.path.dirname(os.path.abspath(__file__))




# def getTTS(text1,text2):
#     data = stream_elements.requestTTS(f'{text1} . . . . . . . {text2}', stream_elements.Voice.en_US_Wavenet_D.value)
#     with open(os.path.join(fileDir, "./tts.mp3"), '+wb') as file:
#         file.write(data)
#     time.sleep(2)
#     return






# from elevenlabs.client import ElevenLabs
# VOICE_ID  = "cgSgspJ2msm6clMCkdW9"  # Jessica :contentReference[oaicite:0]{index=0}
# MODEL_ID  = "eleven_flash_v2_5"             # v3 alpha model id :contentReference[oaicite:1]{index=1}
# FORMAT    = "mp3_44100_128"         # 44.1 kHz, 128 kbps
# client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
# def getTTS(text1, text2) -> str:
#     """Convert *text* to speech and write an MP3 file."""
#     audio_chunks = client.text_to_speech.convert(
#         text=f'{text1} . {text2}',
#         voice_id=VOICE_ID,
#         model_id=MODEL_ID,
#         output_format=FORMAT,
#     )
#     with open(os.path.join(fileDir, "./tts.mp3"), "wb") as f:
#         for chunk in audio_chunks:     # iterate over the chunks
#             if chunk:                  # ignore keep-alive blanks
#                 f.write(chunk)
#     time.sleep(2)

def getTTS(text1,text2):
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=f'{text1} . . . . . . . {text2}')

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Chirp3-HD-Leda"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=1.4
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(os.path.join(fileDir, "./tts.mp3"), "wb") as out:
        out.write(response.audio_content)
        # print('Audio content written to "tts.mp3"')
    time.sleep(2)
#
getTTS('im going to read the title!',"then i'll read the description!")
import re
from google.cloud import texttospeech

from ..configuration.config import QUESTION_AUDIO_PATH


class TTS():
    def __init__(self, context=""):
        self.context = context
        # Set google TTS config
        # Instantiates a client
        self.client = texttospeech.TextToSpeechClient()
        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        self.voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
        # Select the type of audio file you want returned
        self.audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    def text_to_speach(self):
        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(text=self.context)
        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = self.client.synthesize_speech(
            synthesis_input, self.voice, self.audio_config)

        with open("./TTS.mp3", 'wb') as out:
            out.write(response.audio_content)

        file = open("./TTS.mp3", "rb").read()
        return file

    def make_question_audio(self, title):
        synthesis_input = texttospeech.types.SynthesisInput(text=self.context)

        response = self.client.synthesize_speech(
            synthesis_input, self.voice, self.audio_config)

        with open("/home/jake/question_audio_files/" + title + ".mp3", 'wb') as out:
            out.write(response.audio_content)

        return True

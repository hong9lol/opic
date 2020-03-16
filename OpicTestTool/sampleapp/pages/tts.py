from google.cloud import texttospeech

from ..configuration.config import QUESTION_AUDIO_PATH

from datetime import datetime


class TTS():
    def __init__(self, context):
        self.context = context
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US', ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
        self.audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    def text_to_speach(self):
        synthesis_input = texttospeech.types.SynthesisInput(text=self.context)

        response = self.client.synthesize_speech(
            synthesis_input, self.voice, self.audio_config)

        file_name = './tts_' + self._getTime() + '.mp3'
        with open(file_name, 'wb') as out:
            out.write(response.audio_content)

        file = open(file_name, "rb").read()
        return file, file_name

    def make_question_audio(self, title='TTS'):
        synthesis_input = texttospeech.types.SynthesisInput(text=self.context)

        response = self.client.synthesize_speech(
            synthesis_input, self.voice, self.audio_config)

        with open(QUESTION_AUDIO_PATH + title + '.mp3', 'wb') as out:
            out.write(response.audio_content)

        return True

    def _getTime(self):
        now = datetime.now()
        time = now.strftime('%Y-%m-%d_%H:%M:%S')
        return time

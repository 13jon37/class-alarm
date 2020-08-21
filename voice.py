import gtts, time, os

from playsound import playsound

from gtts import gTTS

class Voice:

	def __init__(self):
		self.audio_class = "class.mp3"
		self.audio_awake = "awake.mp3"

	def play_voice_class(self):
		playsound(self.audio_class)

	def play_voice_awake(self):
		playsound(self.audio_awake)
import gtts, time

from playsound import playsound

class Voice:

	def __init__(self):
		self.audio = "class.mp3"

	def play_voice(self):
		playsound(self.audio) # Play mp3 file already downloaded
		time.sleep(3.5)
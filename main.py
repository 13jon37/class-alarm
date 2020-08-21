import time, os

from time import strftime

from music import Music

from voice import Voice

# I am bad at OOP
# Program will play voice saying "time for class" and a video
# at the designated time

class Alarm:

	def __init__(self):
		self.AWAKE_TIME = "10:48"
		self.CLASS_TIME = "11:35"
		self.music = Music()
		self.voice = Voice()
		
	def run(self):
		while True:
			current_time = strftime("%H:%M", time.localtime())
			full_time = time.asctime(time.localtime())

			if current_time == self.AWAKE_TIME:
				print(f"Time to wake up! {current_time}\n")
				print(f"{full_time}")

				# Call voice & music functions
				self.voice.play_voice_awake()
				time.sleep(3000)
				self.music.play_music()
			elif current_time == self.CLASS_TIME:
				print(f"Time for class! {current_time}\n")
				print(f"{full_time}")

				self.voice.play_voice_class()
			else:
				print(f"{full_time}")
			os.system("clear")		# ('cls') for windwows



if __name__ == '__main__':
	ai = Alarm()
	ai.run()


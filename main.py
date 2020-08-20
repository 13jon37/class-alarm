import time, os

from time import strftime

from music import Music

from voice import Voice

# I am bad at OOP
# Program will play voice saying "time for class" and a video
# at the designated time

class Alarm:

	def __init__(self):
		self.CLASS_TIME = "06:17"
		self.music = Music()
		self.voice = Voice()
		
	def run(self):
		while True:
			current_time = strftime("%H:%M", time.localtime())
			full_time = time.asctime(time.localtime())

			if(current_time == self.CLASS_TIME):
				print(f"Time for class! {current_time}\n")
				print(f"{full_time}")

				# Call voice & music functions
				self.voice.play_voice()
				self.music.play_music()

				os.system("clear")
			else:
				print(f"{full_time}")
				os.system("clear")
		time.sleep(1)


if __name__ == '__main__':
	ai = Alarm()
	ai.run()


import time, os, pyfiglet

from time import strftime

from music import Music

from voice import Voice

# I am bad at OOP
# Program will play voice saying "time for class" and a video
# at the designated time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Alarm:

	def __init__(self):
		self.ascii_banner = pyfiglet.figlet_format("Hello!!")
		self.ascii_banner2 = pyfiglet.figlet_format("1337 Alarm")
		self.AWAKE_TIME = "06:30"
		self.CLASS_TIME = "09:25"
		self.music = Music() 
		self.voice = Voice()
		
	def run(self):
		os.system('resize -s 12 55') # Resize terminal window on mac

		# Print Hello in ascii art in blue color
		print(f"{bcolors.OKBLUE}{self.ascii_banner}")
		time.sleep(3)
		while True:
			# Print "1336 Alarm" ascii banner in blue
			print(f"{bcolors.OKBLUE}{self.ascii_banner2}")

			# Get & store H&M of local time as a string
			current_time = strftime("%H:%M", time.localtime())
			# Get and store local time fully as in Day, Mnth, Hours, mins, etc.
			full_time = time.asctime(time.localtime())

			if current_time == self.AWAKE_TIME:
				print(f"Time to wake up! {bcolors.WARNING}{current_time}\n")
				print(f"{bcolors.OKGREEN}{full_time}")

				# Call voice & music functions
				self.voice.play_voice_awake()
				self.music.play_music()
			elif current_time == self.CLASS_TIME:
				print(f"Time for class!{bcolors.WARNING}{current_time}\n")
				print(f"{full_time}")

				self.voice.play_voice_class()
			else:
				print(f"{bcolors.OKGREEN}{full_time}")
			time.sleep(1) # To stop console flickering
			os.system("clear") # Clear the console ('cls') for windwows



if __name__ == '__main__':
	ai = Alarm()
	ai.run()


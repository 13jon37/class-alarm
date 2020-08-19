import time, gtts, os, pafy, vlc
from time import strftime
from playsound import playsound

TIME_CLASS = "9:30"

def play_sound():
	playsound("class.mp3") # Play mp3 file already downloaded
	time.sleep(3.5)

def music():
	url = "https://www.youtube.com/watch?v=s8qWpCMgecs"
	video = pafy.new(url)
	best = video.getbest()
	playurl = best.url
	Instance = vlc.Instance()
	player = Instance.media_player_new()
	Media = Instance.media_new(playurl)
	Media.get_mrl()
	player.set_media(Media)
	player.play()
	time.sleep(120)


def main():
# In Loop: Grab local time (only hours&mins) 
# If local time = class time playvoice
	while True:
		HM = strftime("%H:%M", time.localtime())
		# Get local time and convert to string
		if(str(HM) == TIME_CLASS):
			print(f"Time for class! {HM}")
			play_sound()
			music()
			os.system("clear")
		else:
			print(f"Not time for class. {HM}")
			os.system("clear")
	time.sleep(1)

if __name__ == '__main__':
	main()


	
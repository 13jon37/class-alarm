import pafy, vlc, time

class Music:

	def __init__(self):
		self.URL = "https://www.youtube.com/watch?v=4WkcYaAecOQ"

	def play_music(self):
		video = pafy.new(self.URL)
		best = video.getbest()
		playurl = best.url
		Instance = vlc.Instance()
		player = Instance.media_player_new()
		Media = Instance.media_new(playurl)
		Media.get_mrl()
		player.set_media(Media)
		player.play()
		time.sleep(120)
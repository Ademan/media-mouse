class Amarok(object):
	dcop = None
	def __init__(self):
		if not Amarok.dcop:
			Amarok.dcop = __import__("dcop")
		dcop = Amarok.dcop

		self.client = dcop.DCOPClient()
		self.player = dcop.DCOPRef("amarok", "player")
		self.player.setDCOPClient(self.client)
		self.client.attach()
	def next(self): self.player.call("next()")
	def prev(self): self.player.call("prev()")

	def toggle_play(self): self.player.call("playPause()")
	def volume_up(self, amount): self.player.call("volumeUp()")
	def volume_down(self, amount): self.player.call("volumeDown()")

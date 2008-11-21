class Banshee(object):
	bus_name = "org.bansheeproject.Banshee"
	playback_iface = "/org/bansheeproject/Banshee/PlaybackController"
	player_iface = "/org/bansheeproject/Banshee/PlayerEngine"
	volume_base = 0
	volume_range = 100
	dbus = None
	def __init__(self):
		if not Banshee.dbus:
			Banshee.dbus = __import__("dbus")
		dbus = Banshee.dbus

		self.bus = bus = dbus.SessionBus()

		self.playback = bus.get_object(Banshee.bus_name,
					Banshee.playback_iface)

		player = bus.get_object(Banshee.bus_name,
					Banshee.player_iface)

		self.player = dbus.Interface(player, "org.bansheeproject.Banshee.PlayerEngine")

	def _vol(self):
		#print "Volume: ", self.iplayer.GetVolume()
		return self.player.GetVolume()
	def _volstep(self, amount):
		return Banshee.volume_base + (amount * Banshee.volume_range)
	def _setvol(self, amount):
		self.player.SetVolume(Banshee.dbus.UInt16(self._vol() + self._volstep(amount)))
	def volume_up(self, amount):
		self._setvol(amount)
	def volume_down(self, amount): 
		self._setvol(-amount)
	def next(self): self.playback.Next(False)
	def prev(self): self.playback.Previous(False)
	def toggle_play(self): self.player.TogglePlaying()

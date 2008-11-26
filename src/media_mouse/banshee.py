# Copyright 2008 Daniel Roberts
# This file is part of Media Mouse.
# 
# Media Mouse is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2.
# 
# Media Mouse is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Media Mouse.  If not, see <http://www.gnu.org/licenses/>.

class Banshee(object):
	bus_name = "org.bansheeproject.Banshee"
	playback_iface = "/org/bansheeproject/Banshee/PlaybackController"
	player_iface = "/org/bansheeproject/Banshee/PlayerEngine"
	volume_base = 0
	volume_range = 100
	dbus = None

	@staticmethod
	def import_dbus():
		if not Banshee.dbus:
			Banshee.dbus = __import__("dbus")
		return Banshee.dbus

	@staticmethod
	def is_active():
		dbus = Banshee.import_dbus()

		session_bus = dbus.SessionBus()
		bus = session_bus.get_object("org.freedesktop.DBus", "/org/freedesktop/DBus")

		return bus.NameHasOwner(Banshee.bus_name)

	def __init__(self):
		dbus = Banshee.import_dbus()

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

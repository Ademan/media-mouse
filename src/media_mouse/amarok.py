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

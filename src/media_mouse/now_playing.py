
import pygtk
pygtk.require('2.0')
import gtk

class NowPlayingWindow(gtk.Widget):
	def __init__(self):
		gtk.Widget.__init__(self)
		self.image = None
		self.song = ''
		self.artist = ''
		self.set_flags(self.flags() | gtk.NO_WINDOW) # unsure of this

		self.connect("expose-event", NowPlayingWindow.expose)

	def expose(self, event): pass
	def change_art(self, image):
		self.image = image
		#re-expose

	def change_song(self, song, artist):
		self.song = song
		self.artist = artist
		#re-expose
	
	def change_all(self, image, song, artist):
		self.image = image
		self.song = song
		self.artist = artist
		#re-expose

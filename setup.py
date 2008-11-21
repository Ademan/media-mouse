#! /usr/bin/env python

from setuptools import setup, find_packages
from os.path import join

setup(
	name = "media-mouse",
	version = "0.2",
	description = """A small python program designed to turn your wireless mouse into a remote control for your favorite media players (so long as your favorite media player is either Banshee or Amarok, support for more players is hopefully on the way though... MPRIS compliant players first, then probably Rhythmbox and others after that)""",
	scripts = [join("src", "mediamouse")],
	package_dir = {'' : "src"},
	packages = find_packages("src"),
	author = "Daniel \"Ademan\" Roberts",
	author_email = "Ademan555@gmail.com"
	)

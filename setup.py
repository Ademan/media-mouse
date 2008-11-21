#! /usr/bin/env python

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

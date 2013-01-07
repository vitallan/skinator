import os
import shutil
import sys
from os.path import join, exists
from lib.ReplaceGuy import ReplaceGuy

class CopyGuy:

	visited = []
	source = "base"
	destination = "outputs/"
	configHolder = None #thats a dependency injection... me and my addictions with java :(. Problaby in python it's not a good idea, but today i don't know
	
	def __init__(self, configHolder):
		self.configHolder = configHolder
		self.destination += configHolder.master_output_folder
	
	def copy_file(self, src, dest):
		replaceGuy = ReplaceGuy(self.configHolder)
		for path, dirs, files in os.walk(src, topdown=True):
			if path not in self.visited:
				for di in dirs:
					self.copy_file(join(path, di), join(dest,  replaceGuy.replacePlaceHolders(di)))
				if not exists(dest):
					os.makedirs(dest)
				for fi in files:
					new_path = join(path, fi)
					shutil.copy(new_path, dest)
					#to ignore the image files
					if  (".js" in new_path or
						".tpl" in new_path or
						".html" in new_path or
						".css" in new_path  or
						".vm" in new_path or
						".inc" in new_path or
						".xml" in new_path or
						".txt" in new_path):
						replaceGuy.createReplacedFile(join(dest, fi))
				self.visited.append(path)
	
	def create_copy(self):
		if exists(self.destination):
			shutil.rmtree(self.destination)
		self.copy_file(self.source, self.destination)
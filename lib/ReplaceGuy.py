from tempfile import mkstemp
from shutil import move
from os import remove, close

class ReplaceGuy:

	configHolder = None #Hell, another dependency injection. Somebody stops me <o>

	def __init__(self, configHolder):
		self.configHolder = configHolder
	
	def createReplacedFile(self, pathToFile): 
		#thats dirty, im creating a new temp file, replacing the placeholders, then removing the old one
		#i know, i should have done this in CopyGuy, but that would hurt the OO, the way it is now
		fh, abs_path = mkstemp()
		print(pathToFile)
		new_file = open(abs_path,'w')
		old_file = open(pathToFile)
		for line in old_file:
			new_file.write(self.replacePlaceHolders(line))
		new_file.close()
		close(fh)
		old_file.close()
		remove(pathToFile)
		move(abs_path, pathToFile)

	def replacePlaceHolders(self, line):
		returnString = ""
		arr = []
		for index in self.configHolder.configs.keys():
			if "{{"+index+"}}" in line:
				returnString = line.replace("{{"+index+"}}", self.configHolder.configs[index])
			else:
				returnString = line
		return returnString
		
from tempfile import mkstemp
from shutil import move
from os import remove, close

class ReplaceGuy:

	configHolder = None #Hell, another dependency injection. Somebody stops me <o>

	def __init__(self, configHolder):
		self.configHolder = configHolder
	
	def createReplacedFile(self, pathToFile): 
		#thats dirty, im creating a new temp file, replacing the placeholders, then removing the old one
		#i know, i should have done this in CopyGuy, but that would hurt the OO, the way it is now (would?)
		fh, abs_path = mkstemp()
		new_file = open(abs_path,'w')
		old_file = open(pathToFile)
		for line in old_file:
			new_file.write(self.replacePlaceHolders(line))
		new_file.close()
		close(fh)
		old_file.close()
		remove(pathToFile)
		move(abs_path, self.replacePlaceHolders(pathToFile))

	def replacePlaceHolders(self, line):
		returnString = line
		arr = []
		for index in self.configHolder.configs.keys():
			if "{{"+index+"}}" in line:
				returnString = returnString.replace("{{"+index+"}}", self.configHolder.configs[index])
		return returnString
		
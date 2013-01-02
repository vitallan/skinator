from array import *
import configparser
import os

class ConfigHolder:

	master_output_folder = "";

	configs = {} 
	
	def __init__(self, path_to_config_file):
		config = configparser.SafeConfigParser()
		config.read(path_to_config_file)
		self.master_output_folder += config.get('folder_options','master_output_folder')
		options = config.options('variables')
		for index in options:
			self.configs[index] = config.get('variables',index)
	
import sys
import os
from lib.CopyGuy import CopyGuy
from lib.ConfigHolder import ConfigHolder



if len(sys.argv) > 1 and sys.argv[1] != None:
	configFile = sys.argv[1]
	if os.path.isfile('config/' + configFile + '.ini'):
		print('Usando arquivo ' + configFile + ' para config')
		baseConfigFile = 'config/' + configFile + '.ini'
	else:
		print('Arquivo ' + configFile + ' nao encontado, usando base_config')
		baseConfigFile = 'config/base_config.ini'
else:
	print('Nenhum arquivo informado como parametro, usando base_config')
	baseConfigFile = 'config/base_config.ini'

configHolder = ConfigHolder(baseConfigFile);

copyGuy = CopyGuy(configHolder)
copyGuy.create_copy()
from lib.CopyGuy import CopyGuy
from lib.ConfigHolder import ConfigHolder

configHolder = ConfigHolder('config/base_config.ini');

copyGuy = CopyGuy(configHolder)
copyGuy.create_copy()
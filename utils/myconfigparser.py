import configparser
from pathlib import Path

cfgFile = 'qa.ini'
cfgFileDir = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath((cfgFile))

config.read(CONFIG_FILE)

def getURL():
    return  config['automation_online']['url']

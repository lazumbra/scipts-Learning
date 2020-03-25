import configparser

config = configparser.ConfigParser()
config.read('config.ini')

delimiter = config['SINACOR']['delimiter']
inputFilepath = config['SINACOR']['inputFilepath']
outputFilepath = config['SINACOR']['outputFilepath']
filteredFilepath = config['SINACOR']['filteredFilepath']

print('delimiter', delimiter)
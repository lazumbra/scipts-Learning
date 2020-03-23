from os import listdir
from os.path import isfile, join

import json
import pprint

input_logs = '/home/jefferson/Downloads/conjunto_sessions/'
files_input = '/home/jefferson/Downloads/conjunto_sessions'
onlyfiles = [f for f in listdir(files_input) if isfile(join(files_input, f))]

for i in range(len(onlyfiles)):

	num_lines = sum(1 for line in open(input_logs + onlyfiles[i]))
	with open(input_logs + onlyfiles[i], 'r') as fp:

		for line in fp.readlines():
			l = line.find('{')
			json_line = line[l : ].strip()

			if l == -1:
				print('invalid line: ' + line.strip())
				continue

			info = json.loads(json_line)

            casa = 0

			if info['op'] == 'list_strategies':
				for strategy in info['strategies']:
					print('broker_name: ' + strategy['broker_name'])
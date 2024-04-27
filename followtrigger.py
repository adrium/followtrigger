import re
import subprocess

def main(config: dict):
	p = subprocess.PIPE
	follow = subprocess.Popen(config['follow'], stdout = p, stderr = p)

	while True:
		line = follow.stdout.readline().decode().strip()

		for name, regex in config['watches'].items():
			if regex['search'].search(line):
				print(f'Matched {name} for {line}')
				subject = regex['subject'].search(line).group(1)
				trigger = config['trigger'].format(subject = subject, name = name)
				print(f'Execute {trigger}')
				subprocess.run(['sh', '-c', trigger])
				break

if __name__ == '__main__':
	import json
	import sys
	config = {}

	with open(sys.argv[1]) as f:
		config = json.load(f)

	for t in config['watches'].values():
		for k, v in t.items():
			t[k] = re.compile(v)

	main(config)

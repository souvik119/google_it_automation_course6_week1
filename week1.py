#!/usr/bin/env python3

from PIL import Image
import os

path = '/home/student-00-1e8f072ef81d/images'
for filename in os.listdir(path):
	if filename[0] != '.':
		name = filename + '.jpeg'
		print(filename)
		print('################################################')
		print(name)
		img = Image.open(os.path.join(path, filename))
		img.rotate(270).resize((128,128)).convert('RGB').save("/opt/icons/{}".format(name))


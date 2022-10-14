#!/usr/bin/python3

import sys
import os 
import shutil
import pathlib


HELP = "init.py PROJECT_NAME"
DIR_FILTER = [".git"]


def project_name():
	return sys.argv[1]


CONFIG_MAP = {
	"@PROJECT_NAME@": project_name(),
}


def dir_filter(dirname):
	for d in DIR_FILTER:
		if d in dirname:
			return False

	return True


def files_iter(root):
	for dirname, subdirs, files in os.walk(root):
		if not dir_filter(dirname):
			continue

		for fname in files:
			path = pathlib.Path(os.path.join(dirname, fname))

			yield str(path)


def file_configure(file_name):
	try:
		with open(file_name, 'w') as f:
			content = f.read()

			for k, v in CONFIG_MAP.items():
				content = content.replace(k, v)

			f.write(content)
	except Exception as e:
		print(str(e))


def main():
	os.rename("PROJECT_NAME", project_name())
	os.chdir(project_name())
	os.rename("PROJECT_NAME", project_name())
	os.chdir("..")

	for f in files_iter("."):
		file_configure(f)

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print(HELP)
	elif sys.argv[1] == "h":
		print(HELP)
	else:
		main()

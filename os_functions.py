import os
import sys

#File path for config file
def find_config_directory():
	global slash
	current_dir = os.getcwd()
	config_dir = f"{current_dir}{slash}config{slash}config.txt"
	return config_dir

#Detects user current os for file management
def os_path_detection():
	global slash
	slash = "/"
	default_path = ""

	if sys.platform.startswith("linux"):
		default_path = "/home/"
		slash = "/"

	if sys.platform.startswith("win32"):
		default_path = "C:\\"
		slash = "\\"

	if sys.platform.startswith("darwin"):
		default_path = "/home/"
		slash = "/"

	return default_path
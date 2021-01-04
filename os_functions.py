import os
import sys
import getpass

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

#Detects user OS
def os_detection():
	user_os = ""
	if sys.platform.startswith("linux"):
		user_os = "linux"

	if sys.platform.startswith("darwin"):
		user_os = "mac"

	if sys.platform.startswith("win32"):
		user_os = "windows"

	return user_os

#Default file path for music in downloads folder for now
def song_location():
	global user 
	user = getpass.getuser()
	user_os = os_detection()

	song_path = ""
	if user_os == "linux" or user_os == "mac":
		song_path = f"/home/{user}/Downloads/"

	if user_os == "windows":
		song_path = f"C:\\Users\\{user}\\Downloads\\"

	return song_path

import os
import sys
import getpass

#File path for config file
def find_config_directory():
	global slash
	current_dir = os.getcwd()
	config_dir = f"{current_dir}{slash}config{slash}config.txt"
	return config_dir

#Path for playlist files
def find_playlist_directory():
	global slash
	current_dir = os.getcwd()
	playlist_dir = f"{current_dir}{slash}playlists{slash}"
	return playlist_dir

#Detects user current os for file management
def os_path_detection():
	user_os = _os_detection()
	default_path = ""

	if user_os == "linux" or user_os == "mac":
		default_path = "/home/"

	if user_os == "windows":
		default_path = "C:\\"

	return default_path

#Function for initializing filesystem slash/backslash
def slash_init():
	user_os = _os_detection()
	global slash
	slash = ""

	if user_os == "linux" or user_os == "mac":
		slash = "/"

	if user_os == "windows":
		slash = "\\"

	return slash

#Detects user OS
def _os_detection():
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
	user_os = _os_detection()

	song_path = ""
	if user_os == "linux" or user_os == "mac":
		song_path = f"/home/{user}/Downloads/"

	if user_os == "windows":
		song_path = f"C:\\Users\\{user}\\Downloads\\"

	return song_path

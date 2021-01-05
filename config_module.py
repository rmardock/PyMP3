from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir
import os_functions
import sys
import os

#combine this file with check_config.py to form config module

#Scans listWidget for songs into song_list list
def scan_list(self):
	song_list =[]
	for i in range(self.listWidget.count()):
		song_list.append(self.listWidget.item(i).text())
	_update_config(song_list)

#Updates config file when new songs are added
def _update_config(song_list):
	current_dir = os_functions.find_config_directory()
	config = open(current_dir, "w+")

	#Writes each song to new line in config file
	for i in range(0, len(song_list)):
		tmp_str = str(song_list[i])
		config.write(f"{tmp_str}\n")

	config.close()

#Checks if config file is present
#If config is present, load data
def check(self):
	#os_functions.os_path_detection()
	config_path = os_functions.find_config_directory()

	#If config file exists
	if os.path.exists(config_path):
		config = open(config_path, "r")

		#Read through each line in config file
		while True: 
			song_name = config.readline()

			if not song_name:
				break

			song_name = song_name.replace("\n", "")

			#Add songs songs to listWidget from previous session(s)
			self.listWidget.addItem(song_name)

		config.close()
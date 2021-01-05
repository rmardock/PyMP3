import os
import sys
import os_functions
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir

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
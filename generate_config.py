from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir
import pygame
import getpass
import os_functions
import os

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
		print(song_list[i])
		tmp_str = str(song_list[i])
		config.write(f"{tmp_str}")

	config.close()
import pygame 
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets


#possibly use phonon library instead of pygame


def play():
	pygame.mixer.music.load()
	var.set()
	pygame.mixer.music.play()

def stop():
	pygame.mixer.music.stop()

def pause():
	pygame.mixer.music.pause()

def unpause():
	pygame.mixer.music.unpause()


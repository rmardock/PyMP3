from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir
import pygame
import getpass
import generate_config
import os_functions
import check_config

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 470, 71, 34))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 470, 71, 34))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 470, 61, 34))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 470, 61, 34))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 470, 71, 34))
        self.pushButton_7.setObjectName("pushButton_7")

        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(200, 430, 391, 20))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 341, 20))
        self.label_2.setObjectName("label_2")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 530, 160, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(50)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 510, 161, 18))
        self.label_3.setObjectName("label_3")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(210, 60, 381, 351))
        self.graphicsView.setObjectName("graphicsView")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(600, 60, 181, 32))
        self.comboBox.setObjectName("comboBox")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(667, 100, 111, 34))
        self.pushButton_5.setObjectName("pushButton_5")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 151, 451))
        self.listWidget.setObjectName("listWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Player"))
        self.pushButton.setText(_translate("MainWindow", "▶️"))
        self.pushButton_2.setText(_translate("MainWindow", "⏮️"))
        self.pushButton_3.setText(_translate("MainWindow", "⏹️"))
        self.pushButton_4.setText(_translate("MainWindow", "⏭️"))
        self.pushButton_6.setText(_translate("MainWindow", "Select a song"))
        self.label_2.setText(_translate("MainWindow", "SongName"))
        self.label_3.setText(_translate("MainWindow", "Volume"))
        self.pushButton_5.setText(_translate("MainWindow", "Select Playlist"))
        self.pushButton_7.setText(_translate("MainWindow", "⏸️"))

    def initUI(self, MainWindow):
        #File browsing button connections
        self.pushButton_6.clicked.connect(self.browse_songs)
        self.pushButton_5.clicked.connect(self.browse_playlist)#add ability to create playlists and add to them

        #Media control button connections
        self.pushButton.clicked.connect(self.play)
        self.pushButton_7.clicked.connect(self.pause)
        self.pushButton_3.clicked.connect(self.stop)
        self.listWidget.itemSelectionChanged.connect(self.selection_change)
        self.horizontalSlider.valueChanged.connect(self.adjust_volume)

        #Initialize user name for file path
        global user
        user = getpass.getuser()

        #Initialize variable for unpausing with play button
        global pause
        pause = "off"

        check_config.check(self)

        #Initialize pygame mixer
        pygame.mixer.init()
        #Initial volume for player
        pygame.mixer.music.set_volume(0.5)

    #In Graphic box, load default image 
    #Future addition --> allow/search for album art and display in grapic box

    #Build similar function for loading playlists

    #Add minus button to remove song from list
    #change 'Select a song' button to +
    def browse_songs(self):
        #default_path = os_detection()
        default_path = os_functions.os_path_detection()
        file_name = QFileDialog.getOpenFileName(None, "Select a song:", default_path, "Song Files (*.wav)")
        global song_name
        global user
        song_name = file_name[0];
        print(song_name)
        song_name = song_name.replace(f"/home/{user}/Downloads/", "")
        song_name = song_name.replace(".wav", "")

        self.listWidget.addItem(song_name)

        #Adds songs to list and writes to config file
        generate_config.scan_list(self)

        #use file_name to start playing song
        #future functionality --> add song to song list left and read file from list to play songs

    def browse_playlist(self): #browse playlist -> playlist is a folder of songs created from this player
        default_path = "/home/"
        folder_name = QFileDialog.getExistingDirectory(None, "Select a playlist (folder):", default_path)
        
        #build method to show all folder files (playlist songs) in left column and show playlists (folders) in right column
        #allow selection of folders present in right column to load songs into left column
        #allow user to provide playlist path or use application default path

    def play(self):
        global pause
        global song_name
        #global user
        if pause == "off":
            song_path = os_functions.song_location()
            song = f'{song_path}{song_name}.wav'

            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)

        if pause == "on":
            pygame.mixer.music.unpause()
            pause = "off"

    def pause(self):
        pygame.mixer.music.pause()

        #For unpausing using the play button
        global pause
        pause = "on"

    def stop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        global pause 
        global play
        play = "off"
        pause = "off"

    def selection_change(self):
        global song_name
        tmp_song_name = ([i.text() for i in self.listWidget.selectedItems()])
        song_name = tmp_song_name[0]
        song_name = song_name.replace("['", "")
        song_name = song_name.replace("']", "")
        
        global pause 
        pause = "off"

    def adjust_volume(self):
        #Volume values between 0 and 1.0
        volume = self.horizontalSlider.value()
        if volume == 0:
            volume = 0

        else:
            volume = volume / 100
        pygame.mixer.music.set_volume(volume)


    #Build a class to write a config file to store user songs after application closes
    #Build function in class to read and initialize data on startup
    #If no config (initial startup) --> continue regular startup

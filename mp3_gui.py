from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir
import pygame
import getpass
import config_module
import os_functions

#Rename all QWidget elements
class Ui_MainWindow(object):

    #Initialize UI elements
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
        self.pushButton_6.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 470, 71, 34))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 20, 71, 21))
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(630, 20, 61, 21))
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(710, 20, 61, 21))
        self.pushButton_10.setObjectName("pushButton_10")

        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(200, 430, 391, 20))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 58, 18))
        self.label.setObjectName("label")

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

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(630, 0, 58, 18))
        self.label_4.setObjectName("label_4")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(210, 60, 381, 351))
        self.graphicsView.setObjectName("graphicsView")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 520, 141, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 151, 451))
        self.listWidget.setObjectName("listWidget")

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(625, 51, 151, 451))
        self.listWidget_2.setObjectName("listWidget_2")

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
        self.pushButton_6.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Tracks"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Volume"))
        self.label_4.setText(_translate("MainWindow", "Playlists"))
        self.pushButton_5.setText(_translate("MainWindow", "Add to playlist"))
        self.pushButton_7.setText(_translate("MainWindow", "⏸️"))
        self.pushButton_8.setText(_translate("MainWindow", "-"))
        self.pushButton_9.setText(_translate("MainWindow", "+"))
        self.pushButton_10.setText(_translate("MainWindow", "-"))

    def initUI(self, MainWindow):
        #File browsing button connections
        self.pushButton_6.clicked.connect(self._browse_songs)
        #self.pushButton_5.clicked.connect(self._browse_playlist) 

        #add ability to create playlists and add to them

        #Media control button connections
        self.pushButton.clicked.connect(self._play)
        self.pushButton_7.clicked.connect(self._pause)
        self.pushButton_3.clicked.connect(self._stop)
        self.listWidget.itemSelectionChanged.connect(self._selection_change)
        self.horizontalSlider.valueChanged.connect(self._adjust_volume)

        #Initialize user name for file path
        global user
        user = getpass.getuser()

        #Initialize variable for unpausing with play button
        global pause
        pause = "off"

        #Initialize file system slash/backslash
        global slash 
        slash = os_functions.slash_init()

        #Check for config file and initialize data if config file exists
        config_module.check(self)

        #Initialize pygame mixer
        pygame.mixer.init()
        #Initial volume for player
        pygame.mixer.music.set_volume(0.5)

    #In Graphic box, load default image 
    #Future addition --> allow/search for album art and display in grapic box

    #Build similar function for loading playlists

    def _browse_songs(self):
        default_path = os_functions.os_path_detection()
        file_name = QFileDialog.getOpenFileName(None, "Select a song:", default_path, "Song Files (*.wav)")
        
        global song_name
        global user
        
        song_path = os_functions.song_location()
        song_name = file_name[0];
        song_name = song_name.replace(f"{song_path}", "")
        song_name = song_name.replace(".wav", "")

        #Update listWidget column
        self.listWidget.addItem(song_name)

        #Adds songs to list and writes to config file
        config_module.scan_list(self)

    def _play(self):
        global pause
        global song_name
        if pause == "off":
            song_path = os_functions.song_location()
            song = f'{song_path}{song_name}.wav'

            #Shows loaded song name
            self.label_2.setText(f"{song_name}")

            #Load song and play 
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)

        #If unpausing, resume
        if pause == "on":
            pygame.mixer.music.unpause()
            pause = "off"

    def _pause(self):
        pygame.mixer.music.pause()

        #For unpausing using the play button
        global pause
        pause = "on"

    def _stop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        global pause 
        global play
        play = "off"
        pause = "off"

    #Function for when new song is selected in listWidget
    def _selection_change(self):
        global song_name
        tmp_song_name = ([i.text() for i in self.listWidget.selectedItems()])
        song_name = tmp_song_name[0]
        song_name = song_name.replace("['", "")
        song_name = song_name.replace("']", "")
        
        global pause 
        pause = "off"

    def _adjust_volume(self):
        #Volume values between 0 and 1.0
        volume = self.horizontalSlider.value()
        if volume == 0:
            volume = 0

        else:
            volume = volume / 100
        pygame.mixer.music.set_volume(volume)

    def _add_playlist(self):
        #Instead of folder --> possibly make a playlist.txt file and read songs in from there
        return

    def _remove_playlist(self):
        #Code to remove selected folder(or playlists.txt file) and contents
        return
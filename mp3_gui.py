from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir

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

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Player"))
        self.pushButton.setText(_translate("MainWindow", "Play"))
        self.pushButton_2.setText(_translate("MainWindow", "Previous"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_4.setText(_translate("MainWindow", "Next"))
        self.pushButton_6.setText(_translate("MainWindow", "Select a song"))
        self.label_2.setText(_translate("MainWindow", "SongName"))
        self.label_3.setText(_translate("MainWindow", "Volume"))
        self.pushButton_5.setText(_translate("MainWindow", "Select Playlist"))
        self.pushButton_7.setText(_translate("MainWindow", "Pause"))

    def initUI(self, MainWindow):
        self.pushButton_6.clicked.connect(self.browse_songs)
        self.pushButton_5.clicked.connect(self.browse_playlist)#add ability to create playlists and add to them

        #Media control button connections
        #self.pushButton.clicked.connect(self.play)
        #self.pushButton_7.clicked.connect(self.pause)
        #self.pushButton_3.clicked.connect(self.stop)

    """
    def os_detection():
        system_os = platform.system()
        default_path = ""
        
        if system_os == "Linux" or sysetm_os == "Darwin" or system_os == "Java":
            default_path = "/home/"

        if system_os == "Windows":
            default_path = "C:\\"

        return default_path
    """

    def browse_songs(self):
        #default_path = os_detection()
        default_path = "/home/"
        global file_name
        file_name = QFileDialog.getOpenFileName(None, "Select a song:", default_path, "Song Files (*.wav *.mp3)")
        #use file_name to start playing song
        #future functionality --> add song to song list left and read file from list to play songs

    def browse_playlist(self): #browse playlist -> playlist is a folder of songs created from this player
        default_path = "/home/"
        folder_name = QFileDialog.getExistingDirectory(None, "Select a playlist (folder):", default_path)
        #build method to show all folder files (playlist songs) in left column and show playlists (folders) in right column
        #allow selection of folders present in right column to load songs into left column

    def init_music():
        pygame.mixer.init()
        pygame.mixer.music.load(file_name)

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()




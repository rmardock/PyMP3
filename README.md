# PyMP3

---

This is a MP3 player I'm designing in python.
This is currently a work in progress and is not yet finished.

Windows is now supported! 

---

For now, this music player will only use .wav files because pygame does not support (or is rough) with .mp3 files. 

	* If you know of any libraries better suited to audio playback, please let me know!

For now the file path for song files is set to /home/'user'/Downloads/ for linux/mac and C:\Users\'user'\Downloads\ for windows. 

`'user'` in these paths is the current user's username. The application automatically detects and uses the username in file paths.

For now please use the download folder for managing music. Future updates will allow more flexibility

***

### Dependencies

* Python3
* PyQt5
* PyQt5-tools
* pygame
* getpass

---
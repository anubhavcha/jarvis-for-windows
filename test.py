# import sys
# from PyQt5.QtWidgets import QApplication, QWidget

# class TransparentWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Set the window title
#         self.setWindowTitle('Transparent GUI')

#         # Set the window size
#         self.setGeometry(100, 100, 400, 300)

#         # Set the window opacity (0 is fully transparent, 1 is fully opaque)
#         self.setWindowOpacity(0.4)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = TransparentWindow()
#     window.show()
#     sys.exit(app.exec_())


from pydub import AudioSegment
from pydub.playback import play
import playsound

sound_file = "/home/zeno/Desktop/Jarvis/mp3(data)/X2Download.app - Tony's Workshop Music — Productivity Superhero Mix (128 kbps).mp3"
volume_percentage = 0.01  # Set the volume percentage here

# Load the audio file and adjust the volume
sound = AudioSegment.from_file(sound_file, format="mp3")
sound = sound + volume_percentage

# Play the sound file
play(sound)

# Alternatively, you can use the `playsound` module to play the sound file
# playsound.playsound(sound_file, block=True)

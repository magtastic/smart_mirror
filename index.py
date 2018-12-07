from pyicloud import PyiCloudService
from iCloudManager import iCloud
import Tkinter
from motionSensor import MotionSensor

class App:
    def __init__(self):
        self.window = Tkinter.Tk()

        self.isFullscreen = True
        self.window.configure(background="black")
        self.window.attributes("-fullscreen", self.isFullscreen)
        self.window.bind("<Escape>", self.toggleFullscreen)
        self.motionSensor = MotionSensor()

        self.icloud = iCloud()

        self.mainLabel = Tkinter.Label(
            self.window,
            text="No Motion",
            fg="green",
            bg="black",
            font=("FreeMono", 28)
        )
        self.mainLabel.pack()

    def start(self):
        self.listenToMotionSensor()
        self.window.mainloop()

    def motionDetectedGUIUpdate(self, detected):
        if detected:
            self.mainLabel.config(text="Motion Detected")
        else:
            self.mainLabel.config(text="No Motion")

    def toggleFullscreen(self, event=None):
        self.isFullscreen = not self.isFullscreen
        self.window.attributes("-fullscreen", self.isFullscreen)

    def listenToMotionSensor(self):
        motionDetected = self.motionSensor.readSensorData()
        self.motionDetectedGUIUpdate(motionDetected)
        self.window.after(10, self.listenToMotionSensor)


app = App()
app.start()


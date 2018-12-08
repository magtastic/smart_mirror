try:
    import RPi.GPIO as GPIO

    class MotionSensor:
        def __init__(self):
            self.pin_number = 23
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.pin_number, GPIO.IN)

        def readSensorData(self):
            return GPIO.input(self.pin_number) == 1
except:
    print('Not running on rasp...')

    class MotionSensor:
        def readSensorData(self):
            return False

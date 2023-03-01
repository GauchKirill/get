import  RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(22, RPi.GPIO.OUT)
RPi.GPIO.setup(27, RPi.GPIO.IN)

RPi.GPIO.output(22, RPi.GPIO.input(27))
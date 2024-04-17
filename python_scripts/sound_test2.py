#Big sound sensor
import RPi.GPIO as GPIO
import time

print("program started")
print("GPIO Setup")
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def callback(channel):
    if GPIO.input(channel):
        print("Sound Detected")
    else:
        print("Not Detected!!")

print("call detect event , callback")
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

print("Loop started")
while True:
    time.sleep(1)
    

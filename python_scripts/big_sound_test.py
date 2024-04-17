# This Raspberry Pi code was developed by newbiely.com
# This Raspberry Pi code is made available for public use without any restriction
# For comprehensive instructions and wiring diagrams, please visit:
# https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-sound-sensor


import RPi.GPIO as GPIO
from time import sleep

# Set the Raspberry Pi GPIO pin number where the sound sensor is connected
SOUND_SENSOR_PIN = 17

print("program started")
print("GPIO Setup")

# Set the GPIO mode and configure the sound sensor pin as INPUT
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)

sound_threshold = 1
# Initialize the previous state variable with the current state
prev_sound_state = GPIO.input(SOUND_SENSOR_PIN)

try:
    while True:
        # Read the current state of the sound sensor
        sound_state = GPIO.input(SOUND_SENSOR_PIN)

        # Check for a state change (LOW to HIGH or HIGH to LOW)
        if sound_state == sound_threshold:
                print("Sound detected!")
        else:
            print("No Sound")
        # Add a small delay to prevent continuous readings
        sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings when Ctrl+C is pressed
    GPIO.cleanup()
    print("\nExiting the program.")

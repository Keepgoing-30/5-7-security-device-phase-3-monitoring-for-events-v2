import time
import RPi.GPIO as GPIO #Import Raspberry Pi GPIO library
GPIO.setwarnings(False) #Ignore warning now)
GPIO.setmode(GPIO.BOARD) #using physical pin numbering
# Set general purpose Input Output (GPIO) Pin 4 (position 7) to be an input pin and set initial value to be pulled low (off)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False #semaphore variable - that allows us to know whether or not we're ready

while True: #Run forever
    if GPIO.input(7) == GPIO.HIGH and not button_pressed: # this is a key to avoiding duplicate print statements
        print('Someone has pressed the alert button!')
        button_pressed = True
    elif GPIO.input(7)==GPIO.LOW and button_pressed:
        button_pressed = False #reset the semaphore
    time.sleep(0.1) #sleep for 1/10 of one second

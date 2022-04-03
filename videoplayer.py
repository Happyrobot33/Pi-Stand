import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

movie1 = ("/home/pi/Videos/001_button_pressed.mp4")
movie2 = ("/home/pi/Videos/002_button_pressed.mp4")
movie3 = ("/home/pi/Videos/003_button_pressed.mp4")
movie4 = ("/home/pi/Videos/004_button_pressed.mp4")
movie5 = ("/home/pi/Videos/005_button_pressed.mp4")
movie6 = ("/home/pi/Videos/006_button_pressed.mp4")
movieIdle = ("/home/pi/Videos/007_button_pressed.mp4")
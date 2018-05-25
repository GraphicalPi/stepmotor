#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
ControlPin=[17,22,23,24]

for pin in ControlPin:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

Seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]
       
StepCount = len(Seq)
StepDir = 1
WaitTime = 100/float(1000)
StepCounter = 0

for i in range (1024):
  for halfstep in range (8):
    for pin in range (4):
      GPIO.output(ControlPin[pin], Seq[halfstep][pin])
    time.sleep(0.001)

#Polite blinking program

import machine
import time

led = machine.Pin(0,machine.Pin.OUT) #led
txt = input("Blink or no?")  #asks for input
while txt!= "no":
  for i in range(500):
    led.value(1)
    time.sleep(.03)
    led.value(0)
    time.sleep(.03)
  txt = input("Blink or no?")

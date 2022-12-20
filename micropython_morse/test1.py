from machine import Pin
from utime import sleep_ms
from bps_morse import Character

led=Pin(4,Pin.OUT)

x=Character(led,100)

d="hello bps how are you"

for i in d:
  x.morse_out(i)
  print(i)
  sleep_ms(50)
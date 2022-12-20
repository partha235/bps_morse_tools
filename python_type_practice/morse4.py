import pyttsx3
import string as s
import random as r
from time import sleep

x=pyttsx3.init()
while True:
    charac=s.ascii_lowercase
    let=r.choices(charac)
    x.say(str(let))
    x.setProperty('rate',100)
    x.runAndWait()
    sleep(1)
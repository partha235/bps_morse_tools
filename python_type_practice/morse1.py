from time import sleep
import datetime as dt
import turtle as t
import string as s
import random as r

t.pensize(50)
t.screensize(100,100,"green")
t.title("bps_morse-level.1")

while True:
    t.penup()
    sec = dt.datetime.now().second
    t.hideturtle()
    x=r.choice(s.ascii_uppercase)
    t.setx(5)
    t.sety(0)
    t.write(str(sec),font=("Arial",100,"bold"))
    t.setx(-5)
    t.sety(-200)
    t.write(x,font=("Arial",100,"bold"))
    sleep(2)
    t.resetscreen()
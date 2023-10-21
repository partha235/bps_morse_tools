import os
import string as s
import random as r
from time import sleep

ch_n=int(input('enter number of character \n '))

for ch in range(ch_n):
    x=r.choice(s.ascii_uppercase)
    y=r.choice(s.digits)
    z=r.choice(s.punctuation)
    char_lis=[x,y,z]
    char_speak=r.choice(char_lis)
    print("char_speak = "+char_speak)
    try:
        os.system("espeak "+char_speak)
    except:
        pass 
    sleep(1)
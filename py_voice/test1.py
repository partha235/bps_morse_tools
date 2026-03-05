import subprocess
from time import sleep
import random as r

l1 = ["t", "m", "o"]
subprocess.run(["espeak", "-s", "150", "start"])
sleep(1)
while True:
    x = r.choice(l1)
    subprocess.run(["espeak", "-s", "150", x])
    print(x)
    sleep(0.5)
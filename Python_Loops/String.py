import time
import os  # To run Mac system commands

countdown = int(input("Enter countdown time in seconds: "))

while countdown > 0:
    print("Countdown:", countdown)
    time.sleep(1)
    countdown -= 1

print("Time's up!")
os.system("say 'Time is up!!!!!!'")  # Mac will speak this out loud!

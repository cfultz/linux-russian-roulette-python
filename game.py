import os
import random
import time
# Copied from an Instagram post by @engineermemes but originally from
# what appears to be a Twitter account for @programmerstayo. 
# This version, however, is built by me, https://cfultz.com/@cfultz

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'>

# commands for if you lose
reboot = 'shutdown -r now'
rmetc = 'rm -rf /etc'
rmbin = 'rm -rf /bin'
rmrf = 'rm -rf /'

# picking a random cylinder... erm... number
number = random.randint(1,6)

# setting up the guess logic
guess = input("Guess a number between 1 and 6: ")
guess = int(guess)

# it's *click* *click* *click* *BOOM* time

if guess == number:
   print("*CLICK* \nYou win and live to play another round!")
else:
   #os.remove(rmrf)
   os.remove("/root/derp")
   print("*BOOM* \nIt all goes dark...")
   time.sleep(3)
   os.system('reboot')

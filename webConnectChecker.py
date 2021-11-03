import os
import time
from subprocess import Popen

hostname = "google.com"
counter = 0

while True:
    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        time.sleep(60)
    else:
        if counter < 5:
            #TODO turn off radio
            Process=Popen('/home/pi/Desktop/radio/k1.sh %s' % (str(0)), shell=True)
            time.sleep(20)
            #TODO turn on radio
            counter += 1
            Process=Popen('/home/pi/Desktop/radio/k1.sh %s' % (str(1)), shell=True)
            time.sleep(60)
        else:
            counter = 0
            time.sleep(3600)
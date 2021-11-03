import os
import time

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
            time.sleep(20)
            #TODO turn on radio
            counter += 1
            print(hostname, 'is down!')
        else:
            counter = 0
            time.sleep(3600)
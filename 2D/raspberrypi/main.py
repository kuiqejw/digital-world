# set up environment variables
import os
if os.path.isfile('./setup.py'):
    import setup

import fb

from TempReader import TempReader
from PWM        import WaterPump

from helpers    import unblock

temp_reader = TempReader()

def update_temp():

    while 1:
        try:
            temp = temp_reader.next_reading()
            fb.set('temp', temp)
            print 'Temperature set to {}'.format(temp)
        except:
            print 'Failed to set temperature in firebase'

# allows temperature to be constantly updated using a separate thread (non-blocking)
unblock(update_temp)

pump = WaterPump(32, 32)
while 1:
    try:
        power = float( fb.get('power') )
        pump.set_power(power)
        print 'Power set to {}'.format(power)
    except KeyboardInterrupt:
        break
    except Exception, e:
        print 'Failed to retrieve power from firebase'
        print e
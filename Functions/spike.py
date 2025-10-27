""" This program uses string replication and nested loops to draw spikes. """

import time,sys
try:
    while True:
        # Draw lines with increasing length:
        for i in range(1, 9):
            print('-' * (i * i))
            time.sleep(.5)

        for i in range(8, 1, -1):
            print('-' * (i * i))
            time.sleep(.5)
except KeyboardInterrupt:
    sys.exit()


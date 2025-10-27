""" This program will create a back-and-forth zigzag pattern until the user stops it by pressing the Mu editor's Stop button or by pressing CTRL-C.  """

import time, sys
# TODO 10. Wrap everything in a try-except KeyboardInterrupt block so that pressing Ctrl + C stops it cleanly.
try:
    # TODO 1. Initialize an indent variable (e.g. indent = 0).
    indent = 0 # How many spaces to indent

    # TODO 2. Create another variable to track direction (e.g. increasing = True).
    increasing = True # Whether the indentation is increasing or not

    # TODO 3. Start an infinite while True: loop.
    while True:
        # TODO 4. Inside the loop, print spaces before the stars using " " * indent + "********".
        print(" " * indent + "********")

        # TODO 5. Use time.sleep() to slow down the animation.
        time.sleep(0.5)

        # TODO 6. If increasing is True, increment indent by 1 each loop.
        if increasing:
            indent += 1

        # TODO 7. When indent reaches a max limit, switch increasing to False.
        if indent == 6:
            increasing = False

        # TODO 8. If increasing is False, decrement indent.
        if not increasing:
            indent -= 1

        # TODO 9. When indent hits 0 again, switch back to True.
        if indent == 0:
            increasing = True
except KeyboardInterrupt:
    sys.exit()



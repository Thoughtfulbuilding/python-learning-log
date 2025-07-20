import time, sys

try:
    while True: # The main program loop
    # Draw lines with increasing lenth:
        for i in range(1, 9):
            print('-' * (i * i))
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()# Write your code here :-)

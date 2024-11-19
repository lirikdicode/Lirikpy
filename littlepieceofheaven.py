import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_littlepieceofheaven():
    lines = [
        ("'Cause I really always knew that my little crime", 0.2),
        ("Would be cold That's why I got a heater for your thighs", 0.7),
        ("And I know", 0.7),
        ("I know it's not your time", 0.7),
        ("But bye bye", 0.2)
    ]

    delays = [0.4, 0.2, 1.5, 1.5, 1.8]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.12 if i in [] else 0.055)
        custom_sleep(delays[i])
        print()
print_littlepieceofheaven()
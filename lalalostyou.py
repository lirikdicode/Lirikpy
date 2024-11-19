import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_lalalostyou():
    lines = [
        ("All my demons run wild", 0.2),
        ("All my demons have your smile", 0.7),
        ("In the city of angels", 0.7),
        ("In the city of angels", 0.7)
    ]

    delays = [2.4, 2.0, 2.7, 1.4]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.09 if i in [] else 0.09)
        custom_sleep(delays[i])
        print()
print_lalalostyou()
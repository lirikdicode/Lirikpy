import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_birdsofafeather():
    lines = [
        ("Might not be long", 0.2),
        ("But baby I", 0.7),
        ("Don't wanna say goodbye ", 0.7),
        ("Birds of a feather, we should stick together, I know", 0.2),
        ("I said I'd never think I wasn't better alone", 0.2),
        ("Can't change the weather, might not be forever, but", 0.4),
        ("If it's forever, it's even better ", 0.3)
    ]

    delays = [0.8, 2.5, 0.6, 0.65, 0.8, 0.65, 0.8, 2.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.15 if i in [1] else 0.079)
        custom_sleep(delays[i])
        print()
print_birdsofafeather()
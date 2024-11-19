import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_iwantitthatway():
    lines = [
        ("Tell me why", 0.2),
        ("Ain't nothin' but a heartache", 0.7),
        ("Tell me why", 0.7),
        ("Ain't nothin' but a mistake", 0.7),
        ("Tell me why", 0.2),
        ("I never wanna hear you say", 0.2),
        ("I want it that way", 0.4)
    ]

    delays = [0.45, 1.35, 0.45, 1.35, 0.65, 2.1, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.15 if i in [6] else 0.07)
        custom_sleep(delays[i])
        print()
print_iwantitthatway()
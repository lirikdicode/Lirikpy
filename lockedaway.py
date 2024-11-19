import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_anythingyouwant():
    lines = [
        ("I wanna know would you stick around", 0.2),
        ("If I got locked away", 0.7),
        ("And we lost it all today", 0.7),
        ("Tell me honestly", 0.7),
        ("Would you still love me the same?", 0.7),
        ("If I showed you my flaws", 0.2),
        ("If I couldn't be strong", 0.7),
        ("Tell me honestly", 0.2),
        ("Would you still love me the same?", 0.7)
    ]

    delays = [0.8, 0.8, 1.0, 0.9, 0.8, 0.8, 0.8, 0.8, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.05 if i in [0] else 0.07)
        custom_sleep(delays[i])
        print()
print_anythingyouwant()
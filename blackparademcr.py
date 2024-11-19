import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_blackparade():
    lines = [
        ("So paint it black", 0.2),
        ("And take it back, let's shout it loud and clear", 0.7),
        ("Defiant to the end we hear the call", 0.7),
        ("To carry on", 0.7),
        ("We'll carry on", 0.7),
        ("And though you're dead and gone believe me", 0.2),
        ("Your memory will carry on", 0.2),
        ("We'll carry on", 0.7),
        ("And though you're broken and defeated", 0.2),
        ("Your weary widow marches", 0.2)
    ]

    delays = [0.4, 1.3, 1.8, 1.4, 1.4, 1.4, 1.6, 1.4, 1.6, 2.5]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.09 if i in [3,4,6,7] else 0.05)
        custom_sleep(delays[i])
        print()
print_blackparade()
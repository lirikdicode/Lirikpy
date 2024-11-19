import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_thatswhatiwant():
    lines = [
        ("These days I'm way too alone", 0.2),
        ("And I'm known for giving love away but", 0.7),
        ("I want", 0.7),
        ("Someone to love me", 0.7),
        ("I need", 0.7),
        ("Someone who needs me", 0.2),
        ("'Cause it don't feel right when it's late at night", 0.2),
        ("And it's just me and my dreams", 0.4),
        ("So I want", 0.2),
        ("Someone to love", 0.4),
        ("That's what I f*cking want", 0.4)
    ]

    delays = [0.35, 0.5, 2.0, 1.5, 2.1, 2.0, 0.45, 0.7, 2.1, 1.0, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.05 if i in [1,7] else 0.06)
        custom_sleep(delays[i])
        print()
print_thatswhatiwant()
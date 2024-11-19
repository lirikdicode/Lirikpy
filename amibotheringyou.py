import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_amibotheringyou():
    lines = [
        ("But then out of blue", 0.2),
        ("A spark or two seemed to generate", 0.7),
        ("Now i'm bothering you", 0.7),
        ("It's bothering me", 0.7),
        ("What can i do?", 0.7),
        ("What should I do?", 0.2),
        ("We're not too far", 0.2),
        ("Look where we are", 0.4),
        ("Bothering me", 0.2),
        ("Bothering you", 0.4)
    ]

    delays = [0.9, 1.15, 1.0, 0.85, 0.55, 0.5, 0.45, 0.7, 0.7, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.06 if i in [6,7] else 0.08)
        custom_sleep(delays[i])
        print()
print_amibotheringyou()
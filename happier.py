import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_happier():
    lines = [
        ("I hope you're happy", 0.2),
        ("I wish you all the best, really", 0.7),
        ("Say you love her baby", 0.7),
        ("Just not like you love me", 0.7),
        ("And think of me fondly when your hands are on her", 0.7),
        ("I hope you're happy", 0.2),
        ("But don't be happier", 0.2)
    ]

    delays = [2.2, 0.6, 0.45, 0.45, 0.4, 0.35, 1.6]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.08 if i in [3,4,5] else 0.1)
        custom_sleep(delays[i])
        print()
print_happier()
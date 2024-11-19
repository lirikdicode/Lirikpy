import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_payphone():
    lines = [
        ("Where all the plans we made for two", 0.2),
        ("If happy ever after did exist", 0.7),
        ("I would still be holding you like this", 0.7),
        ("All those fairytailes are full of sh*t", 0.7),
        ("One more f*cking love song I'll be sick", 0.2),
        ("Now I'm at the payphone", 0.2)
    ]

    delays = [1.5, 2.1, 1.9, 1.5, 1.5, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.065)
        custom_sleep(delays[i])
        print()
print_payphone()
import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_diewithasmile():
    lines = [
        ("So I'ma love you every night like it's the last night", 2.0),
        ("Like it's the last night", 0.7),
        ("Cause sometimes I look in her eyes", 1.0),
        ("And that's where i find", 1.2),
        ("A glimpse of us", 0.5), 
        ("And I try to fall for her touch", 1.0),
        ("But i'm thinking of", 1.0),
        ("The way it was", 1.0)
    ]

    delays = [0.5, 0.8, 0.6, 0.7, 1.4, 0.8, 1.0, 1.6]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.15 if i == 8 else (0.1 if i in [2,4,5,7] else 0.06))
        custom_sleep(delays[i])
        print()
print_diewithasmile()
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
        ("If the world was ending, I'd wanna be next to you . . .", 1.0),
        ("If the party was over", 1.2),
        ("And our time on Earth", 0.5),
        ("Was through . . . ", 1.0),
        ("I'd wanna hold you", 1.0),
        ("Just for a while", 1.0),
        ("And die", 1.2),
        ("With a smile", 1.0),
        ("If the world was ending, I'd wanna be next", 1.0),
        ("To you...", 1.0)
    ]

    delays = [0.5, 1.0, 3.5, 1.5, 1.1, 2.0, 1.5, 1.6, 1.0, 1.5, 0.9, 1.5]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.15 if i == 8 else (0.1 if i in [2,5,8,10,11] else 0.06))
        custom_sleep(delays[i])
        print()
print_diewithasmile()
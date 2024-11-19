import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_aboutyou():
    lines = [
        ("And there was something 'bout you that now ", 0.2),
        ("I can't remember", 0.7),
        ("It's the same damn thing that made", 0.7),
        ("My heart surrender", 0.7),
        ("And I miss you on a train,", 0.2),
        ("I miss you in the morning, I", 0.2),
        ("Never know what to think about", 0.4),
        ("I think about you", 0.4)
    ]

    delays = [0.6, 0.7, 1.3, 0.7, 1.0, 1.8, 1.0, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.06)
        custom_sleep(delays[i])
        print()
print_aboutyou()
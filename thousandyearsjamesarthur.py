import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_somebodypleasure():
    lines = [
        ("I love you for a thousand more", 0.2),
        ("And all along", 0.7),
        ("I believed", 0.7),
        ("I would find you", 0.7),
        ("Time has brought your heart to me", 0.7),
        ("I have loved you", 0.2),
        ("For a thousand years", 0.2),
        ("I'd love you for a thousand more", 0.7)
    ]

    delays = [2.7, 0.45, 0.45, 0.7, 0.4, 0.5, 1.6, 1.8]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.06 if i in [4] else 0.08)
        custom_sleep(delays[i])
        print()
print_somebodypleasure()
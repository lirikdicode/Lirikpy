import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_cancer():
    lines = [
        ("That if you say", 2.8),
        ("Good-bye today", 2.7),
        ("I'd ask you to be true", 5.0),
        ("Cause the hardest part of this", 4.2),
        ("Is leaving you", 8.0),
        ("Cause the hardest part of this", 4.2),
        ("Is leaving you", 8.0)
    ]

    delays = [1.2, 1.7, 2.2, 1.8, 5.2, 1.9, 4.5]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.17 if i in [2,4,6] else 0.11)
        custom_sleep(delays[i])
        print()
print_cancer()
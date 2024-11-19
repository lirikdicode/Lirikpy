import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_fixyou():
    lines = [
        ("When you lose something you cannot replace", 0.2),
        ("Tears stream", 0.7),
        ("Down your face", 0.7),
        ("I promise you I will learn from my mistakes", 0.2)
    ]

    delays = [2.8, 1.5, 2.5, 1.2]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.09)
        custom_sleep(delays[i])
        print()
print_fixyou()
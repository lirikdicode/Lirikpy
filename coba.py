import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_mcr():
    lines = [
        ("When you go", 4.0),
        ("And would you even turn to say", 5.0),
        ("I don't love you", 1.5),
        ("Like I did", 1.8),
        ("Yesterday", 4.0)
    ]
    
    delays = [1.7, 1.9, 0.7, 0.7, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.15)
        custom_sleep(delays[i])
        print()
print_mcr()
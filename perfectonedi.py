import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_perfectonedi():
    lines = [
        ("If you like to do the things you know that we shouldn't do", 1.0), #1
        ("Baby, I'm perfect", 0.7), #2
        ("Baby, I'm perfect for you", 1.0), #3
        ("And if you like midnight driving with the windows down", 0.2), #4
        ("And if you like going places we can't even pronounce", 0.2), #5
        ("If you like to do whatever you've been dreaming about", 0.2), #6
        ("Baby, you're perfect", 0.2), #7
        ("Baby, you're perfect", 0.2), #8
        ("So let's start right now", 0.2) #9
    ]

    delays = [0.6, 1.2, 0.5, 0.6, 1.0, 0.65, 1.7, 0.8, 0.7]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.07)
        custom_sleep(delays[i])
        print()
print_perfectonedi()
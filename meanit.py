import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_meanit():
    lines = [
        ("If you don't mean it", 0.2),
        ("Hurry home, let's never leave the house", 0.7),
        ("Let's stay in bed while all our friends go out", 0.7),
        ("Why you let those words come out of your mouth?", 0.2),
        ("You've been staring at me with a heart of doubt", 0.2)
    ]

    delays = [0.3, 2.3, 2.2, 2.2, 2.6]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.06)
        custom_sleep(delays[i])
        print()
print_meanit()
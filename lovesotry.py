import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_lovestory():
    lines = [
        ("Cause you were romeo I was a scarlet letter", 0.2),
        ("And my daddy said, Stay away from juliet", 0.7),
        ("But you were everything to me I was begging you please don't go", 0.7),
        ("And I said", 0.7),
        ("Romeo take me somewhere we can be alone", 0.2),
        ("Ill be waiting, all there's left to do is run", 0.2),
        ("You'll be the prince and I'll be the princess", 0.7),
        ("Its a love story", 0.7),
        ("Baby Just say yes", 0.2)
    ]

    delays = [0.6, 0.8, 1.9, 1.0, 1.5, 0.8, 0.7, 0.7, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.065)
        custom_sleep(delays[i])
        print()
print_lovestory()
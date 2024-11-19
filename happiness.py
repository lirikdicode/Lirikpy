import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_happiness():
    lines = [
        ("Will you still be proud?", 2.0),
        ("Proud of me, and my", 2.7),
        ("Short list of accomplishments", 2.0),
        ("Me and my lack of new news", 2.2),
        ("Me and my selfishness", 1.0),
        ("Or me and myself", 1.0),
        ("Wish you nothing but a happy", 1.2),
        ("New version of you", 1.0)
    ]

    delays = [4.5, 1.0, 1.8, 4.0, 0.8, 0.65, 0.8, 2.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.11)
        custom_sleep(delays[i])
        print()
print_happiness()
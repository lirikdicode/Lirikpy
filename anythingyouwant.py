import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_anythingyouwant():
    lines = [
        ("The same song", 0.2),
        ("On repeat", 0.7),
        ("You can call me anything you want", 0.7),
        ("It's fine", 0.7),
        ("By me...", 0.7),
        ("Number two", 0.2),
        ("Out of three", 0.7),
        ("He says that it's his favorite", 0.2),
        ("And I can't disagree", 0.7)
    ]

    delays = [1.4, 1.4, 1.9, 1.9, 1.8, 1.5, 1.8, 1.8, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.12 if i in [2,3,4,5,6,8] else 0.08)
        custom_sleep(delays[i])
        print()
print_anythingyouwant()
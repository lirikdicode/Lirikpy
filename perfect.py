import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_perfect():
    lines = [
        ("Listening to our favorite song", 2.0),
        ("I have faith in what i see", 2.7),
        ("Now I Know I have met an angel", 2.0),
        ("In person", 2.2),
        ("And she looks", 0.5),
        ("Perfect", 0.5),
        ("I don't deserve this", 2.0),
        ("You look", 1.0),
        ("Perfect", 1.2),
        ("Tonight", 2.2)
    ]

    delays = [0.7, 1.0, 2.0, 1.4, 1.0, 1.0, 1.0, 0.8, 0.5, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.15 if i in [5,6,7,8] else 0.08)
        custom_sleep(delays[i])
        print()
print_perfect()
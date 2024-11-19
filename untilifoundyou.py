import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_untilifoundyou():
    lines = [
        ("Oh, I used to say", 0.2),
        ("I would never fall in love again until I found her", 0.7),
        ("I said, 'I would never fall unless it's you I fall into'", 0.7),
        ("I was lost within the darkness, but then I found her", 0.2),
        ("I found you....", 0.2),
    ]

    delays = [1.7, 2.2, 2.2, 2.0, 1.6]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.3 if i in [4] else 0.09)
        custom_sleep(delays[i])
        print()
print_untilifoundyou()
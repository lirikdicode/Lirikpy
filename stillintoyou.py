import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_untilifoundyou():
    lines = [
        ("Let 'em wonder how we got this far", 0.2),
        ("'Cause i don't really need to wonder at all", 0.7),
        ("Yeah after all this time", 0.7),
        ("i'm still into you", 0.2)
    ]

    delays = [1.0, 0.9, 1.4, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.12 if i in [3] else 0.06)
        custom_sleep(delays[i])
        print()
print_untilifoundyou()
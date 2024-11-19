import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_canibehim():
    lines = [
        ("When the lights come on", 0.2),
        ("And I'm on my own", 0.7),
        ("Will you be there to sing it again", 0.7),
        ("Can I be the one you talk about", 0.2),
        ("In all your stories", 0.2),
        ("Can I be him ?", 0.4)
    ]

    delays = [0.3, 0.3, 2.2, 0.8, 2.6, 0.4]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.06)
        custom_sleep(delays[i])
        print()
print_canibehim()
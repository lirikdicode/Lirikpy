import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_birdsofafeather():
    lines = [
        ("Don't you want me like I want you, baby", 0.2),
        ("Don't you need me like I need you now", 0.7),
        ("Sleep tomorrow but tonight go crazy", 0.7),
        ("All you gotta do is just meet me at the", 0.2),
        ("APT APT", 0.2),
        ("APT APT", 0.4),
        ("APT APT", 0.3)
    ]

    delays = [0.7, 1.0, 0.8, 0.8, 0.6, 0.4, 0.6, 2.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.19 if i in [4,5,6] else 0.06)
        custom_sleep(delays[i])
        print()
print_birdsofafeather()
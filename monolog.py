import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_monolog():
    lines = [
        ("Alasan masih bersama", 2.8),
        ("Bukan", 1.0),
        ("Karena terlanjur lama", 3.0),
        ("Tapi rasanya", 4.2),
        ("Yang masih sama...", 7.0)
    ]

    delays = [1.2, 1.0, 1.7, 2.1, 3.5]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.2 if i == 3 else 0.1)
        custom_sleep(delays[i])
        print()
print_monolog()
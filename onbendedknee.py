import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_birdsofafeather():
    lines = [
        ("And if you come back to me", 0.2),
        ("I'll guarantee", 0.7),
        ("That I'll never let you go", 0.7),
        ("Can we go back to the days our love was strong?", 0.2),
        ("Can you tell me how a perfect love goes wrong?", 0.2)
    ]

    delays = [0.7, 0.8, 1.5, 1.2, 1.0, 0.4]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.13 if i in [3,4] else 0.07)
        custom_sleep(delays[i])
        print()
print_birdsofafeather()
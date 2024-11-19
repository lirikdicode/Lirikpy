import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_theonethatgotaway():
    lines = [
        ("Never planned that one day", 0.2),
        ("I'd be losing you", 0.7),
        ("In another life", 0.7),
        ("I would be your girl", 0.7),
        ("We keep all our promises", 0.2),
        ("Be us against the world", 0.2)
    ]

    delays = [0.45, 1.9, 1.9, 1.4, 1.1, 1.8]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.11 if i in [2,3,4,5] else 0.06)
        custom_sleep(delays[i])
        print()
print_theonethatgotaway()
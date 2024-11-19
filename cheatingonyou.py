import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_cheatingonyou():
    lines = [
        ("I know I said goodbye and baby, you said it too", 0.2),
        ("But when I touch her I feel like I'm cheating on you", 0.7),
        ("I thought that I'd be better when I found someone new", 0.7),
        ("But when I touch her I feel like I'm cheating on you", 0.2)
    ]

    delays = [0.7, 0.9, 0.8, 0.8]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.06)
        custom_sleep(delays[i])
        print()
print_cheatingonyou()
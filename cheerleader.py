import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_cheerleader():
    lines = [
        ("She gives me love and affection", 1.0), #1
        ("Baby, did I mention?", 0.7), #2
        ("You're the only girl for me", 1.0), #3
        ("No, I don't need the next one", 0.2), #4
        ("Mama loves you too", 0.2), #5
        ("She thinks I made the right selection", 0.2), #6
        ("Now all that's left to do", 0.2), #7
        ("Is just for me to pop the question", 0.2), #8
        ("Oh, I think that I found myself a cheerleader", 0.2), #9
        ("She is always right there when I need her", 0.2) #10
    ]

    delays = [0.8, 0.8, 0.6, 0.7, 0.45, 0.52, 0.7, 0.8, 1.2, 0.7]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.05 if i in [5,6] else 0.07)
        custom_sleep(delays[i])
        print()
print_cheerleader()
import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_iris():
    lines = [
        ("And I don't want the world to see me", 0.2),
        ("'Cause I don't think that they'd understand", 0.7),
        ("When everything's made to be broken", 0.7),
        ("I just want you to know who I am", 0.2)
    ]
 
    delays = [1.2, 1.5, 1.6, 0.8]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.08)
        custom_sleep(delays[i])
        print()
print_iris()
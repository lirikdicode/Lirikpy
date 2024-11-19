import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_iwannabeyours():
    lines = [
        ("You call the shots babe", 0.2),
        ("I just wanna be yours", 0.7),
        ("Secrets I have held in my heart", 0.7),
        ("Are harder to hide than i thought", 0.7),
        ("Maybe I just wanna be yours", 0.7),
        ("I wanna be yours", 0.2),
        ("I wanna be yours", 0.7)
    ]

    delays = [0.45, 1.7, 1.25, 0.7, 0.4, 0.4, 1.8]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.15 if i in [] else 0.09)
        custom_sleep(delays[i])
        print()
print_iwannabeyours()
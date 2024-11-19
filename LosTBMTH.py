import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_LosT():
    lines = [
        ("Someone", 0.2),
        ("Tell me", 0.7),
        ("Why... Am... I.. this way?", 0.7),
        ("Stupid medicine not doing anything", 0.7),
        ("What... the...", 0.2), 
        ("Hell is f*cking wrong with me?", 0.7),
        ("I guess there's no remedy", 0.2),
        ("I'm so terribly LosT", 0.7)
    ]

    delays = [0.7, 0.7, 2.1, 0.25, 0.4, 2.4, 0.25, 0.8]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.2 if i in [2,4] else 0.07)
        custom_sleep(delays[i])
        print()
print_LosT()
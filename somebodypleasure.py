import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_somebodypleasure():
    lines = [
        ("It was in a blink of an eye", 0.2),
        ("Find a way how to say goodbye", 0.7),
        ("I've got to take me away", 0.7),
        ("From all sadness", 0.7),
        ("Stitch all my wounds", 0.7),
        ("Confess all the sins", 0.2),
        ("And took all my insecure", 0.7),
        ("When will i got the love", 0.2),
        ("That is so pure", 0.7),
        ("Oh, gotta have to always make sure", 0.2),
        ("That I'm not just", 0.7),
        ("I'm not just somebody's pleasure", 0.7)
    ]

    delays = [1.0, 0.8, 1.7, 2.7, 0.4, 0.4, 1.8, 1.3, 2.5, 1.0, 0.5, 01.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.15 if i in [3,8] else 0.099)
        custom_sleep(delays[i])
        print()
print_somebodypleasure()
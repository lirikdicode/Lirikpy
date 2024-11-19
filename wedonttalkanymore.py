import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_wedonttalkanymore():
    lines = [
        ("Every now and then I think you might want me to", 1.0), #1
        ("Come show up at your door", 0.7), #2
        ("But I'm just too afraid that I'll be wrong", 1.0), #3
        ("Don't wanna know", 0.2), #4
        ("If you're looking into her eyes", 0.2), #5
        ("If she's holding onto you so tight", 0.2), #6
        ("The way I did before", 0.2), #7
        ("I overdosed", 0.2), #8
        ("Should've known your love was a game", 0.2), #9
        ("Now I can't get you out of my brain", 0.2), #10
        ("Oh, it's such a shame", 0.2), #11
        ("That we don't talk anymore", 0.2) #12
    ]

    delays = [0.1, 1.3, 1.3, 0.7, 0.8, 0.65, 1.7, 0.8, 0.7, 0.7, 1.0, 0.8]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.05 if i in [0,4,5,8,9] else 0.07)
        custom_sleep(delays[i])
        print()
print_wedonttalkanymore()
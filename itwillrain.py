import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_itwillrain():
    lines = [
        ("But little darlin' watch me change their minds", 0.2),
        ("Yeah for you I'll try I'll try I'll try I'll try", 0.7),
        ("I'll pick up these broken pieces 'til I'm bleeding", 0.7),
        ("If that'll make you mine...", 0.2),
        ("'Cause there'll be no sunlight", 0.2),
        ("If I lose you, baby", 0.4),
        ("There'll be no clear skies", 0.3),
        ("If I lose you, baby", 0.2),
        ("Just like the clouds", 0.4),
        ("My eyes will do the same", 0.3),
        ("If you walk away", 0.3),
        ("Everyday it'll rain", 0.3),
        ("Rain", 0.3),
        ("Rain yea-a-ah", 0.3)
    ]

    delays = [1.7, 2.2, 1.2, 1.3, 1.6, 1.4, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.09 if i in [1,5,6,7,10,11,12,13] else 0.06)
        custom_sleep(delays[i])
        print()
print_itwillrain()
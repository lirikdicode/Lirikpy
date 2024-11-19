import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_versaceonthefloor():
    lines = [
        ("Don't be confused by my smile", 0.2),
        ("Cause I ain't ever been more", 0.7),
        ("For real", 0.7),
        ("For real...", 0.7),
        ("So just", 0.7),
        ("Turn down the lights", 0.2),
        ("And close the door", 0.2),   
        ("Ooh, I love that dress but you wont need it anymore", 0.7),
        ("No you won't need it no more", 0.2),
        ("Lets just kiss 'till we're naked baby", 0.2),
        ("Versace on the floor", 0.2)
    ]

    delays = [1.2, 0.8, 1.75, 1.25, 0.6, 0.7, 1.6, 1.9, 0.9, 2.5, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.09 if i in [3,4,7] else 0.05)
        custom_sleep(delays[i])
        print()
print_versaceonthefloor()
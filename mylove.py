import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_mylove():
    lines = [
        ("And all my love", 0.2),
        ("I'm holding on forever", 0.7),
        ("Reaching for the love that seems so far", 0.7),
        ("So I say a little prayer", 0.7),
        ("And hope my dreams will take me there", 0.2),
        ("Where the skies are blue", 0.2),
        ("to see you once again, my love", 0.4)
    ]

    delays = [2.1, 1.4, 2.6, 1.6, 0.8, 0.6, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.07 if i in [5] else 0.08)
        custom_sleep(delays[i])
        print()
print_mylove()
import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_everysummertime():
    lines = [
        ("Baby I'd give up anything to travel inside your mind", 0.2),
        ("Baby, I fall in love again come every summertime", 0.7),
        ("My daddy taught me to choose 'em wisely", 0.7),
        ("But you don't have to try", 0.7),
        ("Cuz baby I fall in love every summertime", 0.2)
    ]

    delays = [1.5, 2.1, 0.2, 1.0, 1.5]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.08)
        custom_sleep(delays[i])
        print()
print_everysummertime()
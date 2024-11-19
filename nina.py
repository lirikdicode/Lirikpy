import sys
import time

def custom_sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

def print_nina():
    lines = [
        ("Ini sumpahku padamu tuk biarkanmu", 2.0),
        ("Tumbuh lebih baik", 2.7),
        ("Cari panggilanmu", 2.0),
        ("Jadi lebih baik", 2.2),
        ("Dibanding diriku", 2.0),
        ("Tuk sementara", 2.2),
        ("Kita tertawakan", 2.0),
        ("Berbagai hal", 2.2),
        ("Yang lucu dan lara", 2.0),
        ("Selepas-lepasnya,", 2.2),
        ("Saat dewasa kau kan mengerti..", 8.0)
    ]

    delays = [0.7, 1.0, 1.2, 1.4, 1.4, 1.4, 1.5, 1.0, 1.5, 1.4, 1.0]

    for i, (sentence, delay) in enumerate(lines):
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            custom_sleep(0.08)
        custom_sleep(delays[i])
        print()
print_nina()
import sys
import time
import sleep
def print_mcr() :
    line = [
        ("Well, when you go",3.0),
        ("Don't ever think I'll make you try to stay",5.0)
    ]
    delays=[2, 2.3]

    for i, (line, char_delay) in enumerate(line):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
print_mcr()
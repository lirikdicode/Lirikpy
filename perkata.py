import sys
import time

def print_mcr():
    # Daftar kalimat beserta jeda waktu antar kata (jeda per kata bisa berbeda untuk tiap kalimat)
    lines = [
        ("When you go", 4.0),
        ("And would you even turn to say", 5.0),
        ("I don't love you", 1.5),
        ("Like I did", 1.8),
        ("Yesterday", 4.0)
    ]
    
    # Jeda antar kata untuk tiap kalimat
    word_delays = [
        1.2,  # Jeda antar kata untuk kalimat pertama
        0.65,  # Jeda antar kata untuk kalimat kedua
        0.4,  # Jeda antar kata untuk kalimat ketiga
        0.4,  # Jeda antar kata untuk kalimat keempat
        0.6   # Jeda antar kata untuk kalimat kelima
    ]

    # Jeda antar kalimat
    delays = [0.2, 1.9, 0.75, 1.0, 1.0]

    # Loop untuk mencetak setiap kata dalam kalimat dengan jeda antar kata yang berbeda-beda
    for i, (sentence, delay) in enumerate(lines):
        words = sentence.split()  # Memecah kalimat menjadi kata-kata
        for word in words:
            print(word, end=' ')  # Mencetak setiap kata di baris yang sama
            sys.stdout.flush()
            time.sleep(word_delays[i])  # Jeda antar kata sesuai dengan index kalimat
        time.sleep(delays[i])  # Jeda setelah seluruh kata dalam satu kalimat selesai dicetak
        print()  # Pindah baris setelah seluruh kata dari kalimat selesai

# Memanggil fungsi
print_mcr()

import textdistance as td
import random as rd

def bullscows(guess: str, secret: str) -> (int, int):
    bulls = max(len(guess), len(secret)) - td.hamming(guess, secret)
    cows = td.sorensen_dice(guess, secret) * ((len(guess) + len(secret)) / 2)
    return (bulls, int(cows))

def gameplay(ask: callable, inform: callable, words) -> int:
    secret = rd.choice(words)
    atempt = 0
    while True:
        atempt += 1
        guess = ask("Введите слово: ", words)
        inform("Быки: {}, Коровы: {}", *bullscows(guess, secret))
        if guess == secret:
            return(atempt)

def ask(prompt: str, valid = None) -> str:
    guess = input(prompt)
    if valid:
        while guess not in valid:
            guess = input(prompt)
    return guess

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))
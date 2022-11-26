import string
from secrets import choice
from random import randint


def generator(size, with_num, with_alpha, case_sensitive, with_symbol):
    possibilities = ''
    passwords = []

    if with_num is True:
        possibilities += string.digits
    if with_alpha is True:
        if case_sensitive is True:
            possibilities += string.ascii_letters
        else:
            possibilities += string.ascii_lowercase
    if with_symbol is True:
        possibilities += string.punctuation

    repetitions = randint(8, 16)

    for i in range(repetitions):
        password = ''
        for p in range(size):
            password += choice(possibilities)
        passwords.append(password)

    select = randint(0, repetitions)
    return passwords[select]

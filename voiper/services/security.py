import random


def gen_password():
    size = 21
    tablica = 'abcdefghjkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789'
    return ''.join(random.choice(tablica) for _ in range(size))

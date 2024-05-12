import random

from faker import Faker

fk = Faker(locale='zh-CN')


def get_name():
    return fk.name()


def get_id():
    return random.randint(1000, 3000)


def get_age():
    return random.randint(1, 100)


if __name__ == "__main__":
    print(get_name())
    print(get_id())
import random
import string


def random_lower_str(len: int = 32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=len))


def random_upper_str(len: int = 32) -> str:
    return "".join(random.choices(string.ascii_uppercase, k=len))


def random_code(len: int = 30) -> str:
    return "".join(random.choices(string.ascii_uppercase, k=len))


def random_int(min: int, max: int) -> int:
    return random.randint(min, max)

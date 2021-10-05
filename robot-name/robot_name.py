from string import ascii_uppercase, digits
from os import urandom
import random
class Robot:
    def __init__(self) -> None:
        self.name = self.generate_name()
    @staticmethod
    def generate_name() -> str:
        random.seed(urandom(16))
        return ''.join((
            random.choice(ascii_uppercase),
            random.choice(ascii_uppercase),
            random.choice(digits),
            random.choice(digits),
            random.choice(digits),
        ))
    def reset(self) -> None:
        self.name = self.generate_name()

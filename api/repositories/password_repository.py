import re
import string
from random import choice


def password_is_valid(random_string):
    lower = re.findall('[a-z]', random_string)
    upper = re.findall('[A-Z]', random_string)
    number = re.findall('[0-9]', random_string)
    special = re.findall('[!#$%&*+-<>@_]', random_string)
    if lower and upper and number and special:
        return True
    else:
        return False


class PasswodRepository:
    def __init__(self, size):
        self.size = size

    def generate_random_string(self):
        random_string = ''
        characters = string.digits + string.ascii_letters + '!#$%&*+-<>@_'

        for i in range(self.size):
            random_string += choice(characters)

        return random_string

    def generate_password(self):
        while True:
            random_string = self.generate_random_string()
            if password_is_valid(random_string):
                return random_string

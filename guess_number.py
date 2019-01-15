import random


class GuessNumber:
    """Class that simulates the GuessNumber game"""

    def __init__(self, username):
        """method that initializes guess number class"""
        self.username = username
        self.random_number = GuessNumber.generate_random()

    @staticmethod
    def generate_random():
        """method that generates a randomn number"""
        number = random.randint(1, 20)
        return number

    def check_number(self, num):
        """Method that checks user number input"""
        if self.random_number == num:
            return None
        elif self.random_number > num:
            return "your number is low"
        elif self.random_number < num:
            return "your number is high"

import unittest
from guess_number import GuessNumber


class TestGuessNumber(unittest.TestCase):
    """Test class for GuessNumber"""

    def setUp(self):
        """Setup method for the test case class"""
        self.random_number = 7
        self.new_game = GuessNumber(username="Tom")

    def test_generate_random(self):
        """Method that test generated numbers"""
        number_generated = GuessNumber.generate_random()
        self.assertTrue(type(number_generated), int)
        self.assertTrue(number_generated >= 1)
        self.assertTrue(number_generated <= 20)

    def test_check_number_greater(self):
        """Method that tests when a user inputs a higher number than the correct guess"""
        results = GuessNumber.check_number(self, num=8)
        self.assertEqual(results, "your number is high")

    def test_check_number_less(self):
        """Method that tests when a user inputs a lower number than the correct guess"""
        results = GuessNumber.check_number(self, num=2)
        self.assertEqual(results, "your number is low")

    def test_check_correct_guess(self):
        """Method that tests a correct guess"""
        results = GuessNumber.check_number(self, num=7)
        self.assertEqual(results, None)

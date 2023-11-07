import unittest
from unittest.mock import patch
import main  # Import the code to be tested

'''
    Class to test addition of combination of positive and negativenumbers
'''
class TestMain(unittest.TestCase):

    def test_add_numbers(self):
        with patch('builtins.input', side_effect=['5', '2', '3', '5', '-10', '2']):
            # Simulate user input of '3', '2', '3', and '5'
            sum_result = main.add_numbers()
        self.assertEqual(sum_result, 2)

if __name__ == '__main__':
    unittest.main()

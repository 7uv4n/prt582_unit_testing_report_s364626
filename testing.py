import unittest
from number_guessing_game import MainGame


class TestNumberGuessingGame(unittest.TestCase):
    # MAJOR UNIT TESTING CLASS

    def setUp(self):
        self.number_guessing_game = MainGame()

    def test_match_input_validity(self):
        # Test the functionality to check input validity
        print("\n----Test the functionality to check input validity----")
        # Test with a valid four-digit input
        guess = '1234'
        self.assertTrue(self.number_guessing_game.match_input_validity(guess))
        print("Test Case passed for a valid four-digit input")

        # Test with an invalid string input
        guess = 'invalid_input'
        self.assertFalse(self.number_guessing_game.match_input_validity(guess))
        print("Test Case passed for an invalid string input")

        # Test with an invalid 3-digit input
        guess = '123'
        self.assertFalse(self.number_guessing_game.match_input_validity(guess))
        print("Test Case passed for an invalid 3-digit input")

        # Test with an invalid 5-digit input
        guess = '12345'
        self.assertFalse(self.number_guessing_game.match_input_validity(guess))
        print("Test Case passed for an invalid 5-digit input")

        # Test with an invalid negative integer input
        guess = '-12'
        self.assertFalse(self.number_guessing_game.match_input_validity(guess))
        print("Test Case passed for an invalid negative integer input")

    def test_get_clues(self):
        # Test the functionality of the get_clues function
        print("\n----Test the functionality of the get_clues function----")
        guess = "1243"
        clues = self.number_guessing_game.get_clues(guess)
        self.assertTrue(all(item in ['x', 'o', '#'] for item in clues))
        print("Test case to check whether elements belong to ['x','o','#']")
        self.assertTrue(len(clues) == 4)
        print("Test case to check whether the length of clues list is 4")

    def test_random_number_generation(self):
        # Test if the generated number is within the range of 1000 to 9999
        print("\n---Test if generated number is in the range of 1000-9999---")
        random_number = self.number_guessing_game.generate_random_number()
        self.assertTrue(1000 <= random_number <= 9999)
        print("Test Case: Function to select Number by Computer is passed")

    def test_check_data_types(self):
        # Test to check if all the data types involved are of correct formats
        print("\n---Test to check all variables are in correct data types----")
        self.assertTrue(isinstance(
            self.number_guessing_game.attempts, int
            ))
        print("Test case to check attempts variable is int passed")
        self.assertTrue(isinstance(
            self.number_guessing_game.secret_number, int
            ))
        print("Test case to check secret_number variable is int passed")
        self.assertTrue(isinstance(
            self.number_guessing_game.get_clues("1234"), list
            ))
        print("Test case to check whether the clues variable is list passed")
        print("Test Case: Data Types of variables are in accordance")


if __name__ == '__main__':
    unittest.main()

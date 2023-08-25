"""
NAME: YUVANSHANKAR AZHAGUMURUGAN
STUDENT ID: S364626
PRT582 ASSIGNMENT 2
"""

import random


class MainGame:
    """
    A class representing the main game logic.

    Initiate with a Random generated number and number of attempts
    """
    def __init__(self):
        self.secret_number = self.generate_random_number()
        self.attempts = 0

    @staticmethod
    def generate_random_number():
        """
        Generate a random 4-digit number between 1000 and 9999.
        """
        return random.randint(1000, 9999)

    def match_input_validity(self, guess):
        """
        Check if the input is in valid format.
        """
        return len(guess) == 4 and guess.isdigit()

    def get_clues(self, guess):
        """
        Generate clues for the guessed number from input.
        """
        clues = []
        for i in range(4):
            if str(guess)[i] == str(self.secret_number)[i]:
                clues.append('o')  # Correct digit in correct place
            elif str(guess)[i] in str(self.secret_number):
                clues.append('x')  # Correct digit in wrong place
            else:
                clues.append('#')  # Digit not in the number
        return clues

    def play(self):
        """
        Start the game loop.
        """
        print("""
              Welcome to the Number Guessing Game!
              Hint from Clues:
                o - means the digit is in correct place of the guessed number
                x - means the digit is in wrong place but is in the number
                # - means the digit is not in the number
              """)

        play_again = True
        while play_again:
            # Generate a new secret number
            self.secret_number = self.generate_random_number()
            # Initialise number of attempts to zero
            self.attempts = 0
            while True:
                guess = input("Enter your guess (4-digit number), or type 'quit' to exit:")
                if guess.lower() == 'quit':
                    print(f"The secret number was {self.secret_number}. Thanks for playing!")
                    break

                if not self.match_input_validity(guess):
                    print("Invalid input.")
                    continue

                self.attempts += 1
                clues = self.get_clues(guess)

                if guess == str(self.secret_number):
                    print(f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                    break
                else:
                    print("Clues:", ' '.join(clues))  # Display the clues to the user

            play_again = input("Do you want to play again? (yes/no): ").lower() == 'yes'


if __name__ == "__main__":
    GAME = MainGame()
    GAME.play()

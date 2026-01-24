# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return 0


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
        vowel_count1 = sum(1 for char in player1_word if char in "aeiou")
        vowel_count2 = sum(1 for char in player2_word if char in "aeiou")
        if vowel_count1 > vowel_count2:
            return 1
        elif vowel_count2 > vowel_count1:
            return 2
        else:
            return 0


class RockPaperScissors(WordGame):
    """docstring for RockPaperScissors."""

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
        options = {"paper", "rock", "scissors"}

        # Handle invalid inputs
        if player1_word not in options or player2_word not in options:
            if player1_word not in options and player2_word not in options:
                return 0
            return 1 if player1_word in options else 2

        # Handle ties
        if player1_word == player2_word:
            return 0

        # Define winning combinations for player 1
        player1_wins = {
            ("rock", "scissors"),
            ("scissors", "paper"),
            ("paper", "rock"),
        }

        return 1 if (player1_word, player2_word) in player1_wins else 2

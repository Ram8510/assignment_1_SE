import random
import math
import sys


class RPSGame:
    WIN_COUNT = 5
    RPS = ["rock", "paper", "scissors"]

    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0

    def take_input_from_computer_and_player(self):

        while True:
            user = input(
                "Choose anyone between these three: rock, paper or scissors. Press (q) to quit the game or Press (r) for restart the game \n"
            )
            user = user.lower()
            if user == "r":
                self.main()

            if user == "q":
                sys.exit()

            if user not in self.RPS:
                print("you selected the wrong option")
                continue
            else:
                break

        computer = self.computer_selection()

        if user == computer:
            return (0, user, computer)

        # rock > scissors, scissors > paper, paper > rock
        if self.is_win(user, computer):
            return (1, user, computer)

        return (-1, user, computer)

    def computer_selection(self):
        return random.choice(self.RPS)

    def is_win(self, player, computer):
        # return true is the player beats the computer
        # winning conditions: rock> scissors, scissors > paper, paper > rock
        if (
            (player == "rock" and computer == "scissors")
            or (player == "scissors" and computer == "paper")
            or (player == "paper" and computer == "rock")
            or (player == computer)
        ):
            return True
        return False

    def play_best_of(self):
        self.player_wins = 0
        self.computer_wins = 0

        while self.player_wins < self.WIN_COUNT and self.computer_wins < self.WIN_COUNT:
            result, user, computer = self.take_input_from_computer_and_player()
            # tie
            if result == 0:
                print(
                    "It is a tie. You and the computer have both chosen {}. \n".format(
                        user
                    )
                )
            # you win
            elif result == 1:
                self.player_wins += 1
                print(
                    "You chose {} and the computer chose {}.You won this round.Your total win is {} times \n".format(
                        user, computer, self.player_wins
                    )
                )
            else:
                self.computer_wins += 1
                print(
                    "You chose {} and the computer chose {}. You lost this round sorry.. The computer won {} times\n".format(
                        user, computer, self.computer_wins
                    )
                )

        if self.player_wins > self.computer_wins:
            print(
                "You have won the game total 5 times so hurray you are the winner!! Congratulations :D"
            )
        else:
            print(
                " The computer has won the game total 5 times!! So you Lost. Better luck next time!"
            )

    def main(self):
        print("Restart the game")
        self.play_best_of()


if __name__ == "__main__":
    game = RPSGame()
    game.play_best_of()

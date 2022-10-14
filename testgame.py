import unittest
from rpsgame import RPSGame


class UnitTestRPSGame(unittest.TestCase):
    
    def test_player_wins_computer_with_rock_smashes_scissors(self):
        rpsgame = RPSGame()
        user_action = "rock"
        computer_action = "scissors"
        assert (rpsgame.is_win(user_action, computer_action) == True)

    def test_player_wins_computer_with_paper_smashes_rock(self):
        rpsgame = RPSGame()
        user_action = "paper"
        computer_action ="rock"
        assert (rpsgame.is_win(user_action, computer_action) == True)

    def test_player_wins_computer_with_scissors_smashes_paper(self):
        rpsgame = RPSGame()
        user_action = "scissors"
        computer_action ="paper"
        assert (rpsgame.is_win(user_action, computer_action) == True)
    
    def test_computer_randomly_picks_options(self):
        rpsgame = RPSGame()
        assert (rpsgame.computer_selection() != None) == True

    def test_is_tie(self):
        rpsgame = RPSGame()
        user_action = "rock"
        computer_action ="rock"
        assert (rpsgame.is_win(user_action, computer_action) == True)
    


if __name__ == "__main__":
    unittest.main()

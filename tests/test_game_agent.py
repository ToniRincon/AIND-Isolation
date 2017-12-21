"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player_greedy = sample_players.GreedyPlayer()
        self.player_random = sample_players.RandomPlayer()
        self.player_minimax = game_agent.MinimaxPlayer(search_depth=2)
        self.player_alphabeta = game_agent.AlphaBetaPlayer(search_depth=1, score_fn=game_agent.custom_score_2, timeout=10.)
    '''
    def test_greedy_minimax(self):
        print('Greedy vs Minimax')
        game = isolation.Board(self.player_greedy, self.player_minimax,width=7, height=7)
        winner, history, outcome = game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(game.to_string())
        print("Move history:\n{!s}".format(history))
    
    def test_minimax_greedy(self):
        print('Minimax vs Greedy')
        game = isolation.Board(self.player_minimax, self.player_greedy,width=7, height=7)
        game.apply_move((3, 3))
        winner, history, outcome = game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(game.to_string())
        print("Move history:\n{!s}".format(history))
     
    def test_minimax(self):
        game = isolation.Board(self.player_minimax, self.player_random,width=9, height=9)
        game._board_state=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 32]
        print(game.to_string())
        print(self.player_minimax.get_move(game,lambda: 10000))
    '''    
    def test_alphabeta(self):
        game = isolation.Board(self.player_alphabeta, self.player_random,width=9, height=9)
        game._board_state=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 38, 58]
        print(game.to_string())
        print(self.player_alphabeta.get_move(game,lambda: 10000))
        
if __name__ == '__main__':
    unittest.main()

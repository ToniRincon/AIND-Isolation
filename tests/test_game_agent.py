"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players
import timeit

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player_greedy = sample_players.GreedyPlayer()
        self.player_random = sample_players.RandomPlayer()
        self.player_minimax = game_agent.MinimaxPlayer(search_depth=2)
        self.player_alphabeta = game_agent.AlphaBetaPlayer()
        self.player_human = sample_players.HumanPlayer()
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
    '''     
    def tqqqqest_minimax(self):
        game = isolation.Board(self.player_minimax, self.player_random,width=9, height=9)
        game._board_state=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 32]
        print(game.to_string())
        print(self.player_minimax.get_move(game,lambda: 150))
    
    def test_alphabeta(self):
        game = isolation.Board(self.player_alphabeta, self.player_minimax,width=9, height=9)
        winner, history, outcome = game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(game.to_string())
        print("Move history:\n{!s}".format(history))
    def test_alphabeta2(self):
        game = isolation.Board(self.player_alphabeta, self.player_minimax,width=9, height=9)
        print(game.to_string())
        time_millis = lambda: 1000 * timeit.default_timer()
        move_start = time_millis()
        time_left = lambda : 150 - (time_millis() - move_start)
        print(self.player_alphabeta.get_move(game,time_left))
        print(game.to_string())
    def test_human(self):
        game = isolation.Board(self.player_alphabeta, self.player_human,width=9, height=9)
        winner, history, outcome = game.play(time_limit=10000)
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        
if __name__ == '__main__':
    unittest.main()

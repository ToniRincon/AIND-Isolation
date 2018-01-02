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
        self.player_alphabeta_custom = game_agent.AlphaBetaPlayer(score_fn=game_agent.custom_score_3)
        self.player_alphabeta_improved1 = game_agent.AlphaBetaPlayer(score_fn=sample_players.improved_score)
        self.player_alphabeta_improved2 = game_agent.AlphaBetaPlayer(score_fn=sample_players.improved_score)
        self.player_human = sample_players.HumanPlayer()
    '''
    def test_greedy_minimax(self):
        print('Greedy vs Minimax')
        game = isolation.Board(self.player_greedy, self.player_minimax,width=3, height=3)
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
    
    def test_alphabeta2(self):
        game = isolation.Board(self.player_alphabeta_improved, self.player_alphabeta_custom,width=9, height=9)
        time_millis = lambda: 1000 * timeit.default_timer()
        move_start = time_millis()
        time_left = lambda : 150 - (time_millis() - move_start)
        print(self.player_alphabeta_improved.get_move(game,time_left))
    '''
    def test_alphabeta(self):
        print('Improved vs Improved')
        game = isolation.Board(self.player_alphabeta_improved1,self.player_alphabeta_custom,width=7, height=7)
        winner, history, outcome = game.play()
        if winner==self.player_alphabeta_custom:
            winner = '2'
        else:
            winner = '1'
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print("Move history:\n{!s}".format(history))
             
        
if __name__ == '__main__':
    unittest.main()

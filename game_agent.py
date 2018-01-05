"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random

def board_empy(game):
    '''
    return the percentage of blank spaces in the board
    '''
    blank_spaces = len(game.get_blank_spaces())
    total_spaces = game.width * game.height
    return blank_spaces/total_spaces
       
def in_wall(game,player):
    '''
    return the number of available movement in walls
    '''
    walls = set()
    walls.update([(0, i) for i in range(game.width)])
    walls.update([(i, 0) for i in range(game.height)])
    walls.update([(game.width - 1, i) for i in range(game.width)])
    walls.update([(i, game.height - 1) for i in range(game.height)])
    
    moves = game.get_legal_moves(player)
    
    moves_in_wall = 0
    
    for m in moves:
        if m in walls:
            moves_in_wall += 1

    return moves_in_wall
    
def in_corner(game,player):
    '''
    return the number of available movement in corners
    '''
    corners = set([(0,0),(0,game.width-1),(game.height-1,0),(game.height-1,game.width-1)])
       
    moves = game.get_legal_moves(player)
    
    moves_in_corner = 0
        
    for m in moves:
        if m in corners:
            moves_in_corner += 1
    return moves_in_corner
    

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass

def null_score(game, player):
    """This heuristic presumes no knowledge for non-terminal states, and
    returns the same uninformative value for all other states.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    return 0.


def open_move_score(game, player):
    """The basic evaluation function described in lecture that outputs a score
    equal to the number of moves open for your computer player on the board.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    return float(len(game.get_legal_moves(player)))

def improved_score(game, player, w=1):
    """The "Improved" evaluation function discussed in lecture that outputs a
    score equal to the difference in the number of moves available to the
    two players.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - w*opp_moves)

def center_score(game, player):
    """Outputs a score equal to square of the distance from the center of the
    board to the position of the player.

    This heuristic is only used by the autograder for testing.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(player)
    return float((h - y)**2 + (w - x)**2)
   
def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player prioritizing moves in center
    """
    
    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
        
    own_moves = game.get_legal_moves(player)
    opp_moves = game.get_legal_moves(game.get_opponent(player))
    
    # differece of available moves, the reducer 1.2 prioritizes reducing the movility of the opponent
    score_moves = float(len(own_moves)-1.2*len(opp_moves))
    
    # distance to the center
    w, h = game.width // 2., game.height // 2.
    y, x = game.get_player_location(player)
    score_center = float(abs(h - y) + abs(w - x))
    
    # combination of available moves and penality of distance to center
    score = score_moves+w/(score_center+1)
    
    return score


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player penalizing moves in corner or walls
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
        
    empty =  board_empy(game)
    if empty > 0.5:
        return improved_score(game,player,1.2) - 0.25*in_corner(game,player) - 0.25*in_wall(game,player)
    else:
        # at the end of the game increase penality to movement in border or corners
        return improved_score(game,player,1.2) - 0.5*in_corner(game,player) - 0.5*in_wall(game,player)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player ignorig moves than can be used by the opponent
    """
    
    own_moves = game.get_legal_moves(player)
    opp_moves = game.get_legal_moves(game.get_opponent(player))
    
    if player == game._inactive_player and not opp_moves:
        return float('+inf')
    if player == game._active_player and not own_moves:
        return float('-inf')
    
    return float(len(set(own_moves)-set(opp_moves)) - len(opp_moves))


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=100.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        
        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            best_move = self.minimax(game, self.search_depth)

        except SearchTimeout:
            moves = game.get_legal_moves()
            if moves:
                best_move = moves[0]
            else:
                best_move = (-1, -1)

        # Return the best move from the last completed search iteration
        return best_move
    
    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        
        def min_value(game, depth):
    
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            
            if depth == 0:
                return self.score(game,self)
        
            moves = game.get_legal_moves()
            if not moves:
                return self.score(game,self)
        
            return min(max_value(game.forecast_move(m),depth-1) for m in moves)

        def max_value(game, depth):
   
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
        
            if depth == 0:
                return self.score(game,self)
        
            moves = game.get_legal_moves()
            if not moves:
                return self.score(game,self)
        
            return max(min_value(game.forecast_move(m),depth-1) for m in moves)
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        moves = game.get_legal_moves()
        if not moves:
            return (-1,1)
        return max(moves, key=lambda m: min_value(game.forecast_move(m),depth-1))

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        moves = game.get_legal_moves()
        if not moves:
            return (-1,-1)
        best_move = moves[0]
        if game.move_count == 0:
            best_move = (game.width//2,game.height//2)
            return best_move
        if game.move_count == 1:
            best_move = (game.width//2,game.height//2)
            if best_move in moves:
                return best_move
            else:
                best_move = (game.width//2,game.height//2-1)
                return best_move
        #print('get_move','count:',game.move_count,'init:',best_move)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            depth=1
            while True:
                best_move = self.alphabeta(game, depth)
                depth+=1
                
        except SearchTimeout:
            #print('get_move','count:',game.move_count,'depth:',depth,'timeout')
            pass  # Handle any actions required after timeout as needed
            
        # Return the best move from the last completed search iteration
        #print('get_move','count:',game.move_count,'best_move:',best_move)
        return best_move
        
    def alphabeta_with_helpers(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        
        def min_value(game, depth, alpha, beta):
        
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            moves = game.get_legal_moves()
            
            if depth == 0 or not moves:
                return self.score(game,self)
            
            v = float("inf")
            for m in moves:
                v = min(v,max_value(game.forecast_move(m),depth-1,alpha,beta))
                if v<=alpha:
                    return v
                beta = min(beta,v)
            return v
        
        def max_value(game, depth, alpha, beta):
            
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            
            moves = game.get_legal_moves()
            
            if depth == 0 or not moves:
                return self.score(game,self)
            
            v = float("-inf")
            for m in moves:
                v = max(v,min_value(game.forecast_move(m),depth-1,alpha,beta))
                if v>=beta:
                    return v
                alpha = max(alpha,v)
            return v
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        v_best=float('-inf')
        moves = game.get_legal_moves()
        if not moves:
            return (-1,-1)
        m_best = moves[0]
        
        for m in moves:
            v = min_value(game.forecast_move(m),depth-1,alpha,beta)
            if v>v_best:
                v_best=v
                m_best=m
            alpha = max(alpha,v_best)
        return m_best

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"),maximizer=None):
    
        if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
        
        #main, return movement
        if maximizer is None:
            moves = game.get_legal_moves()
            if not moves:
                return (-1,-1)
            v,m =  self.alphabeta(game,depth,alpha,beta,maximizer=True)
            #print(game.move_count,len(moves),depth,m,v)
            return m
        
        if maximizer:
            # max, return score
            moves = game.get_legal_moves()
            if depth == 0 or not moves:
                return self.score(game,self),(-1,-1)
            
            m_best = moves[0]           
            v_best = float("-inf")
            
            for m in moves:
                v,_ = self.alphabeta(game.forecast_move(m),depth-1,alpha,beta,maximizer=False)
                if v>v_best:
                    v_best=v
                    m_best=m
                if v_best>=beta:
                    return v_best,m_best
                alpha = max(alpha,v_best)
            return v_best,m_best
                
        else:
            # min, return score
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
        
            moves = game.get_legal_moves()
            if depth == 0 or not moves:
                return self.score(game,self),(-1,-1)
            
            m_best = moves[0]
            v_best = float("inf")
            
            for m in moves:
                v,_ = self.alphabeta(game.forecast_move(m),depth-1,alpha,beta,maximizer=True)
                if v<v_best:
                    v_best=v
                    m_best=m
                if v_best<=alpha:
                    return v_best,m_best
                beta = min(beta,v)
            return v_best,m_best
            
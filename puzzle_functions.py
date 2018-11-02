""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them.

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.

def get_current_player(player_one_turn: bool) -> str:
    
    """Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """
    
    if player_one_turn:
        return P1
    else:
        return P2
    
 
    # Complete this function.

def get_winner(P1_score: int, P2_score: int) -> str:
    
    """Return the winner of P1_score and P2_score according to score: P1_WINS, P2_WINS, and TIE.
    >>> get_winner(15, 20)
    'P2_WINS'
    >>> get_winner(20,15)
    'P1_WINS'
    """
    
    if P1_score > P2_score:
        return P1_WINS
    elif P1_score < P2_score:
        return P2_WINS
    else:
        return TIE
    
    
def reverse(word: str) -> str:
    
    """Return the reversed copy of the string.
    >>> reverse(hello)
    olleh
    >>> reverse(baby)
    ybab
    """
    
    return word[::-1]


def get_row(puzzle: str, num_row: int) -> str:
    
    """Return the letters corresponding to the row referred to in puzzle with num_row. 
    >>> get_row('abcd\nefgh\nijkl\n', 2)
    efgh
    >>> get_row('abcd\nefgh\nijkl\n', 1)
    abcd
    """
    
    return puzzle.split("\n")[num_row]


def get_factor(direction: str) -> int:
    
    """Return the multiplicative factor associated with the direction.
    >>>get_factor(UP)
    4
    >>>get_factor(FORWARD)
    1
    """
    
    if direction == UP:
        return 4
    elif direction == DOWN:
        return 2
    elif direction == FORWARD:
        return 1
    elif direction == BACKWARD:
        return 3
    
    
def get_points(direction: str, words_left: int) -> int:
    
    """Return the calculated the points obtained from guessing a word with parameters 
    direction and words left.
    >>>get_points(UP, 1)
    36
    >>>get_points(FORWARD, 6)
    5
    """
    
    if words_left < THRESHOLD:
        points = (2 * THRESHOLD - words_left) * get_factor(direction)
    elif words_left >= THRESHOLD:
        points = THRESHOLD * get_factor(direction)
    elif words_left == 1:
        points = (2 * THRESHOLD - 1) * get_factor(direction)
    return points

def check_guess (puzzle: str, direction: str, get_guess: str, num_colrow: int, words_left: int) -> int:
    
    """Return get_points function iff column_of_words or reversed_guess is in the puzzle in the orientation described by parameters: direction and num_colrow
    >>>check_guess('abcm\nefgo\nijkt\n',UP,tom,4,2)
    28
    >>>check_guess('abct\nefgo\nijkm\n',DOWN,tom,4,2)
    16
    """
    
    column_of_words = get_column(puzzle, num_colrow)
    row_of_words = get_row(puzzle, num_colrow)
    reversed_guess = reverse(get_guess)
    
    if direction == UP:
        if contains(column_of_words, reversed_guess):
            return get_points(direction, words_left)
    elif direction == FORWARD:
        if contains(row_of_words, get_guess):
            return get_points(direction, words_left)
    elif direction == DOWN:
        if contains(column_of_words, get_guess):
            return get_points(direction, words_left)
    elif direction == BACKWARD:
        if contains(row_of_words, reversed_guess):
            return get_points(direction, words_left)
        
    return 0

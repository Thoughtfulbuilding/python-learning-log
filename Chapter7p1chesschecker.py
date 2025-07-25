# Write your code here :-)
board1 = {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'}
board = {}
def isValidChessBoard(board):
    # Define valid squares (a1 to h8)
    valid_squares = [x + y for x in 'abcdefgh' for y in '12345678']

    # Define valid piece types and prefixes
    valid_pieces = ['P', 'K', 'B', 'R', 'Q', 'K']
    valid_prefixes = ['w', 'b']

    # Count pieces for each player
    white_pieces = 0
    black_pieces = 0
    white_pawns = 0
    black_pawns = 0
    white_kings = 0
    black_kings = 0

    # Check each piece and square on the board
    for square, piece in board.items():
        # Check if the square is valid
        if square not in valid_squares:
            return False

        # Check if piece name is valid (starts with 'w' or 'b' followed by valid piece type)
        if not (len(piece) >= 2 and \
        piece[0] in valid_prefixes and \
        piece[1:] in valid_pieces): # Checks that the remaining characters match valid piece
            return False

        # Count pieces and pawns
        if piece[0] == 'w':
            white_pieces += 1
            if piece == 'wP':
                white_pawns += 1
            if piece == 'wK':
                white_kings += 1
        else: # piece[0] == 'b'
            black_pieces += 1
            if piece == 'bP':
                black_pawns += 1
            if piece == 'bK':
                black_kings += 1

    # Check king counts
    if white_kings != 1 or black_kings != 1: # ensures exactly only one white king and one black king
        return False

    # Check piece limits
    if white_pieces > 16 or black_pieces > 16: # white and black pieces dont exceed 16
        return False

    # Check pawn limits
    if white_pawns > 8 or black_pawns > 8: # ensures white and black pawns dont exceed 8
        return False

    return True

print(isValidChessBoard(board1))

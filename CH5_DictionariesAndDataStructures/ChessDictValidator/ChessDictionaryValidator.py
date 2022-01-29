'''
This program contains a simple function that checks is a given dictionay. 
A valid chess board will:
    - have exactly one black and white king
    - at most 16 white pieces and 16 black pieces
    - at most 8 white and black pawns
    - at most 2 white and black bishops/rooks/knights/
    - at most 1 white and black queen
    - have only valid spaces between '1a-8h'
All piece names must begin with 'w'(white) or 'b'(black) followed by 'pawn',
'knight', 'bishop', 'rook', 'queen', or 'king'.  
'''
import time
import random
import pprint

def isValidChessBoard(board:dict)->bool:
    global valid_spaces
    pawn_count, knight_count, bishop_count, rook_count = 0,0,0,0
    queen_count, king_count = 0, 0
    for k, v in board.values():
        if k not in valid_spaces: 
            return False
    return False 

def generateSpaces(valid_cols:list)->list:
    valid_spaces = []
    for col in valid_cols:
        for i in range(1,9):
            valid_spaces.append("{}".format(i)+col)
    return valid_spaces

def generatePieces(valid_pieces:list)->list:
    pieces = []
    for p in valid_pieces:
        if p == 'pawn':
            for i in range(16):
                if i < 8: pieces.append('w'+p)
                else: pieces.append('b'+p)
        elif p == 'knight' or p == 'rook' or p == 'bishop':
            for i in range(4):
                if i < 2: pieces.append('w'+p)
                else: pieces.append('b'+p)
        else:#King or queen
           for i in range(2):
                if i < 1: pieces.append('w'+p)
                else: pieces.append('b'+p)
    return pieces

def generateChessBoard(valid_cols:list, valid_pieces:list)->dict:
    board = {}
    spaces = generateSpaces(valid_cols)
    pieces = generatePieces(valid_pieces)
    random.shuffle(spaces)
    random.shuffle(pieces)
    for i,s in enumerate(spaces):
        num = random.random()
        if i == 0: 
            board[s] = 'wking'
        elif i == 1:
            board[s] = 'bking'
        elif num > 0.5 and len(pieces) > 0:
            board[s] = pieces.pop(0)
        else:
            board[s] = ""
    return board 

valid_pieces = ['pawn','knight', 'bishop', 'rook', 'queen']
valid_cols = ['a','b','c','d','e','f','g','h']

board = generateChessBoard(valid_cols, valid_pieces) 
pprint.pprint(board)
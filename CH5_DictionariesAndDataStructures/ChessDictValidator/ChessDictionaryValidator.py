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

def isValidChessBoard(board:dict, valid_spaces:list, valid_pieces:list)->bool:
    pieces = valid_pieces.copy()
    if 'bking' not in pieces: return False
    if 'wking' not in pieces: return False
    for space, piece in board.items():
        if space not in valid_spaces:
            print("Invalid Space: {}".format(space))
            return False
        if piece not in valid_pieces:
            print("Invalid Piece: {}".format(piece))
            return False
        elif piece == "":
            pass
        elif piece not in pieces:
            print('Too many: {}s'.format(piece))
            return False
        else:
            pieces.remove(piece)
    return True

def generateSpaces(valid_cols:list)->list:
    valid_spaces = []
    for col in valid_cols:
        for i in range(1,9):
            valid_spaces.append("{}".format(i)+col)
    return valid_spaces

def generatePieces(valid_pieces:list)->list:
    pieces = [""]
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

def generateChessBoard(spaces:list, p:list)->dict:
    board = {}
    pieces = p.copy()#need to make a copy of the pieces so that the origonal 
                     #is not modified by the pop() call 
    random.shuffle(spaces)
    random.shuffle(pieces)
    for i,s in enumerate(spaces):
        num = random.random()
        if i == 0: 
            board[s] = 'wking'
            pieces.remove('wking')
        elif i == 1:
            board[s] = 'bking'
            pieces.remove('bking')
        elif num > 0.5 and len(pieces) > 0:
            board[s] = pieces.pop(0)
        else:
            board[s] = ""
    return board 

valid_pieces = ['pawn','knight', 'bishop', 'rook', 'queen', 'king']
valid_cols = ['a','b','c','d','e','f','g','h']

s = generateSpaces(valid_cols)
p = generatePieces(valid_pieces)
board = generateChessBoard(s,p) 
print(isValidChessBoard(board,s,p))
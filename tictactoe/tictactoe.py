"""
tictactoe.py

Created by Philo van Kemenade
"""

import random

class TicTacToe(object):
    """A game of Tic Tac Toe"""
    def __init__(self):
        super(TicTacToe, self).__init__()
        self.playing = True
        self.board = Board()
        self.turn = self.whoStarts()
        print "Welcome to Tic Tac Toe"
    
    def whoStarts(self):
        if random.randint(0,1) == 0:
            return "X"
        else:
            return "O"
    
    # start the game
    def start(self):
        self.evaluate()
        while self.playing:
            print "\n"
            self.board.print_board()
            raw_move = self.get_player_input()
            # parse and check move validity
            move = self.parse_move(raw_move)
            if move:
                [row, col] = move
                self.board.mark_move(row, col, self.get_turn())
                self.switch_turn()
            else:
                print "That's not a valid move, please try again"
                continue

        self.board.print_board()
        if self.hasWinner():
            # previous player won the game
            self.switch_turn()
            print "\nPlayer ", self.get_turn(), " has won! Congrats!"
        else:
            print "That's a draw"
        self.playAgain()
            
        
        
    
    # get current player
    def get_turn(self):
        return self.turn
    
    # switch current player
    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
    # get player's input
    def get_player_input(self):
        print "Current player: ", self.get_turn()
        return raw_input("Please input a move: [row], [column]\n")    
    
    def evaluate(self):
        # check for winner
        # check rows
        for row in self.board.cells:
            if self.lineOf3(row):
                self.playing = False
                return True
        # check cols
        for i in range(3):
            col = [row[i] for row in self.board.cells]
            if self.lineOf3(col):
                self.playing = False
                return True
        # check diagonal
        diag1 = [self.board.cells[i][i] for i in [0,1,2]]
        diag2 = [self.board.cells[i][2-i] for i in [0,1,2]]
        if self.lineOf3(diag1):
            self.playing = False
            return True
        if self.lineOf3(diag2):
            self.playing = False
            return True
        return None
    
    def hasWinner(self):
        pass
    
    def lineOf3(self, cellList):
        '''check if 3 elements cause winner'''
        # check if first element is non-empty
        if cellList[0] != "_":
            # check is all elements in cellList are equal
            if cellList.count(cellList[0]) == len(cellList):
                # return sign
                return True
            else:
                return False
        else:
            return False
    
    def parse_move(self, move):
        try:
            posList = move.split(",", 2)
            [row, col]  = [int(posList[0]), int(posList[1])]
        except:
            print "please specify to integers as [row], [column]"
            return None
        if self.valid_move(row, col):
            return [row, col]            
        else:
            print "that's not a valid move, try again"
            return None
    
    def valid_move(self, row, col):
        # check if position coords are on board
        if row not in [0,1,2] or col not in [0,1,2]:
            return False
        # check whether position is free
        elif self.board.cells[row][col] != "_":
            print "that position is not empty"
            return False
        else:
            return True
    
    def playAgain(self):
        again = raw_input("Would you like to play again? (yes / no)")
        return again.lower().startswith('y')
    
class Board:
    # cells = []
    def __init__(self):
        # self.cells = [[cell() for y in range(3)] for x in range(3)]
        self.cells = [["_" for y in range(3)] for x in range(3)]
        self.turn = "X"
    
    def print_board(self):
        for row in self.cells:
            print row
        
    def mark_move(self, row, col, sign):
        self.cells[row][col] = sign
    
    
def main():
    myGame = TicTacToe()
    myGame.start()

if __name__ == '__main__':
  main()
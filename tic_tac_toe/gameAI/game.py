# Description: This file contains the game logic for the Tic Tac Toe game.
#from .AI import AI
import random
class TicTacToe:
    def __init__(self, ai_instance):
        self.board = [   0, 1, 2, 
                         3, 4, 5, 
                         6, 7, 8
                                    ]
        self.turn = 0
        self.human = "X"
        self.AI = "O"
        self.ai_instance = ai_instance
        self.winner = " "
        

        
    
    def turns(self):
        self.turn += 1



    def check_winner(self, board):
        wins = [ [0, 1, 2], 
                          [3, 4, 5], 
                          [6, 7, 8], 
                          [0, 3, 6], 
                          [1, 4, 7], 
                          [2, 5, 8], 
                          [0, 4, 8], 
                          [2, 4, 6] ]
        winner = None
        available_moves = 0
        for win in wins:
            if board[win[0]] == board[win[1]] == board[win[2]]:
                winner = board[win[0]]
                self.winner = winner
                return winner 
        else:
            for i in board:
                if type(i) == int:
                    available_moves += 1    

        if winner == None and available_moves == 0:
            self.winner = "Draw"
            return "Draw"
            
        return winner 


    def play(self, human_move):
        if self.turn % 2 == 0:
            if random.random() < 0.5:
                ai_move = self.ai_instance.best_AI_move(self.board)
                self.board[ai_move] = self.AI
            else:
            # Make a random move for the AI
                available_moves = [i for i, cell in enumerate(self.board) if isinstance(cell, int)]
                ai_move = random.choice(available_moves)
                self.board[ai_move] = self.AI
        else:
            human_move = int(human_move)
            self.board[human_move] = self.human

        result = self.check_winner(self.board)
        self.winner = result
        self.turns()

        return result


    def get_board(self):
        board_dict = {}
        for i, cell in enumerate(self.board):
            board_dict[f"cell_{i}"] = cell if isinstance(cell, str) else " "

        board_dict["winner"] = self.winner
        return board_dict
    
    
    def get_AI_last_played_move(self):
        return [i for i, cell in enumerate(self.board) if cell == "O"]
    
    def reset_game(self):
        self.board = [   0, 1, 2, 
                         3, 4, 5, 
                         6, 7, 8
                                    ]
        self.turn = 0
        self.winner = " "
        return self.board
    
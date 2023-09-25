# Description: This file contains the AI logic for the Tic Tac Toe game.
import random

class AI:
    def __init__(self):
        self.scores = {"X": 10, 
                       "O": -10, 
                       "Draw": 0}
        self.AI = "X"
        self.human = "O"
        

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
                return winner 
        else:
            for i in board:
                if type(i) == int:
                    available_moves += 1    

        if winner == None and available_moves == 0:
            return "Draw"
            
        return winner 
        

    def best_AI_move(self, board):
        best_score = float("-inf")
        best_move = None
        for i in range(len(board)):
            if type(board[i]) == int:
                board[i] = self.AI
                score = self.minimax(board, 0, False)
                board[i] = i
                if score > best_score:
                    best_score = score
                    best_move = i
            
        return best_move #integer from 0-8
    

    def minimax(self, board, depth, maximizing):
        result = self.check_winner(board)  #X or O or Draw
        if result != None:
            return self.scores[result] - depth
        

        if maximizing:
            best_score = float("-100")
            for i in range(len(board)):
                if type(board[i]) == int:
                    board[i] = self.AI
                    score = self.minimax(board, depth + 1, False)
                    board[i] = i
                    best_score = max(score, best_score)
                
            return best_score
        
        else:

            best_score = float("100")
            for i in range(len(board)):
                if type(board[i]) == int:
                    board[i] = self.human
                    score = self.minimax(board, depth + 1, True)
                    board[i] = i
                    best_score = min(score, best_score)
                    
                
            
            return best_score
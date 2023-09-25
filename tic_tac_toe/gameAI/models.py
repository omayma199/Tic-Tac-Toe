# models.py

from django.db import models

class Tournament(models.Model):
    tournament_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.tournament_name

class TicTacToeGame(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    tic_tac_toe = models.CharField(max_length=100)
    game_date = models.DateField()
    winner = models.CharField(max_length=100)
    loser = models.CharField(max_length=100)

    def __str__(self):
        return self.tic_tac_toe

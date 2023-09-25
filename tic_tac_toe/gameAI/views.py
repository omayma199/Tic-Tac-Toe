from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from .game import TicTacToe
from .AI import AI 
from .models import  Tournament 




ai = AI()
game = TicTacToe(ai)
played_moves = set()
# Create your views here.

def index(response):

    if response.method == "POST":
        # reset button, reset the game
        game.reset_game()
        initial_game_data = game.get_board()
        played_moves.clear()
    

    # AI makes the first move
    game.play(None)
    initial_game_data = game.get_board()
    for move in game.get_AI_last_played_move():
        played_moves.add(move)

    return render(response, "main/base.html", {"game_data": initial_game_data})
   

def Game(request):
   
    if request.method == "POST":
        if "cell_value" in request.POST:
            # User clicked a cell button, process the move and update game state
            cell_value = request.POST.get("cell_value")
            if cell_value not in played_moves:
                played_moves.add(cell_value)
                game.play(cell_value)
                
                #AI move
                game.play(None)
                for move in game.get_AI_last_played_move():
                    played_moves.add(move)
                updated_game_data = game.get_board()

                return render(request, "main/base.html", {"game_data": updated_game_data})
            

    return HttpResponse(status=204)   

def tournament_detail(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    games = tournament.game_set.all()

    return render(request, 'tournament_detail.html', {'tournament': tournament, 'games': games})   



    


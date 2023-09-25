from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Game/', views.Game, name='Game'),
    path('tournament/<int:tournament_id>/', views.tournament_detail, name='tournament_detail'),
]





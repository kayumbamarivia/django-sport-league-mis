from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Team
from .forms import TeamForm

@login_required(login_url="/login/")
def team_list(request):
    teams = Team.objects.all()
    
    for team in teams:
        team.players_list = [player.strip() for player in team.players.split(",")]

    return render(request, 'teams/team_list.html', {'teams': teams})

@login_required(login_url="/login/")
def team_players(request, pk):
    team = get_object_or_404(Team, pk=pk)
    players = [player.strip() for player in team.players.split(",")]

    return render(request, 'teams/team_players.html', {'team': team, 'players': players})

@login_required(login_url="/login/")
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/teams')
    else:
        form = TeamForm()
    return render(request, 'teams/team_form.html', {'form': form})

@login_required(login_url="/login/")
def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('/teams')
    else:
        form = TeamForm(instance=team)
    return render(request, 'teams/team_form.html', {'form': form})

@login_required(login_url="/login/")
def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('/teams') 
    return render(request, 'teams/team_confirm_delete.html', {'team': team})

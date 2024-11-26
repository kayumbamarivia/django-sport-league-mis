from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Team
from .forms import TeamForm
from django.core.paginator import Paginator
from django.http import JsonResponse

# View for listing teams
TEAMS = "/teams"
@login_required(login_url="/login/")
def team_list(request): 
    teams = Team.objects.all()
    paginator = Paginator(teams, 10)
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    
    players = {}
    for team in teams:
        players[team.id] = team.players.all()

    # return render(request, 'teams/team_list.html', {'page_obj': page_obj, 'players': players})
    data = {
        'teams': list(page_obj.object_list.values('id', 'name')),  # Example team data
        'players': players
    }
    return JsonResponse(data)


# View for listing players of a team
@login_required(login_url="/login/")
def team_players(request, pk):
    team = get_object_or_404(Team, pk=pk)
    players = team.players.all()

    # return render(request, 'teams/team_players.html', {'team': team, 'players': players})
    data = {
        'team': {
            'id': team.id,
            'name': team.name,
        },
        'players': list(players.values('id', 'name'))  # Example player data
    }
    return JsonResponse(data)


# View for creating a team
@login_required(login_url="/login/")
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Team created successfully.")
            # return redirect(TEAMS)
            return JsonResponse({'message': 'Team created successfully.'})
    else:
        form = TeamForm()

    # return render(request, 'teams/team_form.html', {'form': form})
    return JsonResponse({'message': 'Invalid request'}, status=400)


# View for updating a team
@login_required(login_url="/login/")
def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            # messages.success(request, "Team updated successfully.")
            # return redirect(TEAMS)
            return JsonResponse({'message': 'Team updated successfully.'})
    else:
        form = TeamForm(instance=team)

    # return render(request, 'teams/team_form.html', {'form': form})
    return JsonResponse({'message': 'Invalid request'}, status=400)


# View for deleting a team
@login_required(login_url="/login/")
def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        # messages.success(request, "Team deleted successfully.")
        # return redirect('/teams')
        return JsonResponse({'message': 'Team deleted successfully.'})
    
    # return render(request, 'teams/team_confirm_delete.html', {'team': team})
    return JsonResponse({'message': 'Invalid request'}, status=400)

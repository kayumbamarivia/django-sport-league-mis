from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import League
from .forms import LeagueForm
from django.core.paginator import Paginator

@login_required(login_url="/login/")
def league_list(request):
    leagues = League.objects.all()
    paginator = Paginator(leagues, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'leagues/league_list.html', {'page_obj': page_obj})

@login_required(login_url="/login/")
def league_detail(request, pk):
    league = get_object_or_404(League, pk=pk)
    return render(request, 'leagues/league_detail.html', {'league': league})

@login_required(login_url="/login/")
def league_create(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('league_list')) 
    else:
        form = LeagueForm()
    return render(request, 'leagues/league_form.html', {'form': form})

@login_required(login_url="/login/")
def league_update(request, pk):
    league = get_object_or_404(League, pk=pk)
    if request.method == 'POST':
        form = LeagueForm(request.POST, instance=league)
        if form.is_valid():
            form.save()
            return redirect(reverse('league_list'))
    else:
        form = LeagueForm(instance=league)
    return render(request, 'leagues/league_form.html', {'form': form, 'league': league })

@login_required(login_url="/login/")
def league_delete(request, pk):
    league = get_object_or_404(League, pk=pk)
    associated_teams = league.teams.all() 

    if request.method == 'POST':
        league.delete()
        return redirect(reverse('league_list'))

    return render(request, 'leagues/league_confirm_delete.html', {'league': league, 'associated_teams': associated_teams})

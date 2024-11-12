from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import League
from .forms import LeagueForm

@login_required(login_url="/login/")
def league_list(request):
    leagues = League.objects.all()
    return render(request, 'leagues/league_list.html', {'leagues': leagues})

@login_required(login_url="/login/")
def league_create(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leagues')
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
            return redirect('/leagues')
    else:
        form = LeagueForm(instance=league)
        # for field in form:
        #   print(f'{field.label}: {field.value()}')
    return render(request, 'leagues/league_form.html', {'form': form, 'league': league })

@login_required(login_url="/login/")
def league_delete(request, pk):
    league = get_object_or_404(League, pk=pk)
    if request.method == 'POST':
        league.delete()
        return redirect('/leagues') 
    return render(request, 'leagues/league_confirm_delete.html', {'league': league})


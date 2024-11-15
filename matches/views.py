from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Match
from .forms import MatchForm
from django.core.paginator import Paginator

@login_required(login_url="/login/")
def match_list(request):
    matches = Match.objects.all()
    paginator = Paginator(matches, 10)  # Show 10 matches per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'matches/match_list.html', {'page_obj': page_obj})


@login_required(login_url="/login/")
def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    return render(request, 'matches/match_detail.html', {'match': match})

@login_required(login_url="/login/")
def match_create(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Match created successfully!")
            return redirect('match_list')
    else:
        form = MatchForm()
    return render(request, 'matches/match_form.html', {'form': form})

@login_required(login_url="/login/")
def match_update(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            messages.success(request, "Match updated successfully!")
            return redirect('match_list')
    else:
        form = MatchForm(instance=match)
    return render(request, 'matches/match_form.html', {'form': form})

@login_required(login_url="/login/")
def match_delete(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        match.delete()
        messages.success(request, "Match deleted successfully!")
        return redirect('match_list')
    return render(request, 'matches/match_confirm_delete.html', {'match': match})

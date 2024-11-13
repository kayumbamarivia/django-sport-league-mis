from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Score
from .forms import ScoreForm

@login_required(login_url="/login/")
def score_list(request):
    scores = Score.objects.all()
    return render(request, 'scores/score_list.html', {'scores': scores})

@login_required(login_url="/login/")
def score_detail(request, pk):
    score = get_object_or_404(Score, pk=pk)
    return render(request, 'scores/score_detail.html', {'score': score})

@login_required(login_url="/login/")
def score_create(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Score created successfully!")
            return redirect('score_list')
    else:
        form = ScoreForm()
    return render(request, 'scores/score_form.html', {'form': form})

@login_required(login_url="/login/")
def score_update(request, pk):
    score = get_object_or_404(Score, pk=pk)
    if request.method == 'POST':
        form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            form.save()
            messages.success(request, "Score updated successfully!")
            return redirect('score_list')
    else:
        form = ScoreForm(instance=score)
    return render(request, 'scores/score_form.html', {'form': form})

@login_required(login_url="/login/")
def score_delete(request, pk):
    score = get_object_or_404(Score, pk=pk)
    if request.method == 'POST':
        score.delete()
        messages.success(request, "Score deleted successfully!")
        return redirect('score_list')
    return render(request, 'scores/score_confirm_delete.html', {'score': score})

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User 
from leagues.models import League 
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import login, logout, get_backends
from users.models import User
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserUpdateForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from teams.models import Team
from reports.models import Report


def home(request):
    # return render(request, 'home.html')
    return JsonResponse({'message': 'Welcome to the Home page'})


@login_required(login_url="/login/")
def analytics(request):
    # total_matches = Match.objects.count()
    # total_teams = Team.objects.count()
    # total_goals = Match.objects.aggregate(Sum('goals'))['goals__sum']
    #
    # top_players = Player.objects.order_by('-goals')[:3]
    # top_teams = Team.objects.order_by('-wins')[:3]
    #
    # upcoming_matches = Match.objects.filter(date__gte=timezone.now()).order_by('date')[:5]
    # recent_matches = Match.objects.filter(date__lte=timezone.now()).order_by('-date')[:5]
    #
    # context = {
    #     'total_matches': total_matches,
    #     'total_teams': total_teams,
    #     'total_goals': total_goals,
    #     'top_players': top_players,
    #     'top_teams': top_teams,
    #     'upcoming_matches': upcoming_matches,
    #     'recent_matches': recent_matches
    # }
    data = {
        'total_matches': 100,  # Placeholder for the total matches
        'total_teams': 20,     # Placeholder for the total teams
        'total_goals': 500,    # Placeholder for total goals
        'top_players': ['Player1', 'Player2', 'Player3'],  # Placeholder for top players
        'top_teams': ['Team A', 'Team B', 'Team C'],      # Placeholder for top teams
        'upcoming_matches': ['Match1', 'Match2'],         # Placeholder for upcoming matches
        'recent_matches': ['Match3', 'Match4']            # Placeholder for recent matches
    }
    return JsonResponse(data)


@login_required(login_url="/login/")
def dashboard(request):
    total_leagues = League.objects.count()
    total_teams = Team.objects.count()
    total_reports = Report.objects.count()
    
    data = {
        'total_leagues': total_leagues,
        'total_teams': total_teams,
        'total_reports': total_reports,
    }
    # return render(request, 'dashboard/auth_dashboard.html', context)
    return JsonResponse(data)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User {user.username} created successfully!")
            
            backend = get_backends()[0]
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            
            login(request, user, backend=user.backend)
            return JsonResponse({'message': f'User {user.username} created and logged in successfully!'})
    else:
        form = CustomUserCreationForm()
    # return render(request, 'users/register.html', {'form': form, 'is_update': False})
    return JsonResponse({'message': 'Invalid request'}, status=400)


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            
            backend = get_backends()[0]
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"

            login(request, user, backend=user.backend)
            return JsonResponse({'message': f'Welcome {user.username}! Logged in successfully.'})

    # return render(request, 'users/login.html', {'form': form})
    return JsonResponse({'message': 'Invalid login credentials'}, status=400)


def user_logout(request):
    logout(request)
    # return redirect('user_login')
    return JsonResponse({'message': 'Logged out successfully'})


@login_required(login_url="/login/")
def user_list(request):
    users = User.objects.all() 
    paginator = Paginator(users, 10)  
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)  
    
    roles = {}
    for user in users:
        roles[user.username] = user.get_role_display()

    data = {
        'total_users': users.count(),
        'users': list(page_obj.object_list.values('username', 'role')),  # Assuming 'role' field is available
        'roles': roles
    }
    # return render(request, 'users/user_list.html', {'page_obj': page_obj, 'roles': roles})
    return JsonResponse(data)


@login_required(login_url="/login/")
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User updated successfully'})

    # return render(request, 'users/register.html', {'form': form, 'is_update': True})
    return JsonResponse({'message': 'Invalid request'}, status=400)


@login_required(login_url="/login/")
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()  
        return JsonResponse({'message': f'User {user.username} deleted successfully'})

    # return render(request, 'users/delete_user.html', {'user': user})
    return JsonResponse({'message': 'Invalid request'}, status=400)


@login_required(login_url="/login/")
def search_results(request):
    query = request.GET.get('q', '')
    if query:
        users = User.objects.filter(username__icontains=query)
        leagues = League.objects.filter(name__icontains=query)
    else:
        users = User.objects.none()
        leagues = League.objects.none()

    data = {
        'query': query,
        'users': list(users.values('username', 'role')),
        'leagues': list(leagues.values('name'))
    }
    # return render(request, 'search_result.html', context)
    return JsonResponse(data)

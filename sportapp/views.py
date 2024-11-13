from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone
from users.models import User
from leagues.models import League
from matches.models import Match
from teams.models import Team
from scores.models import Score
from reports.models import Report
from schedule.models import Schedule

@login_required(login_url="/login/")
def admin_dashboard(request):
    # Handle filtering logic
    date_filter = request.GET.get('date_filter')
    if date_filter:
        matches = Match.objects.filter(date=date_filter)
        reports = Report.objects.filter(generated_at__date=date_filter)
    else:
        matches = Match.objects.all()
        reports = Report.objects.all()

    # Get statistics
    total_users = User.objects.count()
    total_leagues = League.objects.count()
    total_matches = matches.count()
    total_teams = Team.objects.count()

    # Get user role counts
    user_roles_count = User.objects.values('role').annotate(count=Count('role'))

    # Get latest matches and reports
    latest_matches = matches.order_by('-date')[:5]
    latest_reports = reports.order_by('-generated_at')[:5]
    upcoming_matches = matches.filter(date__gte=date.today()).order_by('date')[:5]

    context = {
        'total_users': total_users,
        'total_leagues': total_leagues,
        'total_matches': total_matches,
        'total_teams': total_teams,
        'user_roles_count': user_roles_count,
        'latest_matches': latest_matches,
        'latest_reports': latest_reports,
        'upcoming_matches': upcoming_matches,
    }

    return render(request, 'dashboard/admin_dashboard.html', context)

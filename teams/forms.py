from django import forms
from .models import Team
from users.models import User

STYLES =  'form-input border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
class TeamForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(
        queryset=User.objects.none(), 
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': STYLES,
            'id': 'id_players'
        })
    )

    class Meta:
        model = Team
        fields = ['name', 'coach', 'players']

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': STYLES
        })
        self.fields['coach'].widget.attrs.update({
            'class': STYLES
        })
        self.fields['players'].widget.attrs.update({
            'style': 'width: 100%;'
        })
        current_team = kwargs.get('instance', None)
        if current_team:
            self.fields['coach'].queryset = User.objects.filter(role='coach').exclude(
                coached_teams__isnull=False
            ).union(User.objects.filter(coached_teams=current_team))
        else:
            self.fields['coach'].queryset = User.objects.filter(role='coach', coached_teams__isnull=True)
        if current_team:
            self.fields['players'].queryset = User.objects.filter(role='player').exclude(
                player_teams__isnull=False
            ).union(current_team.players.all())
        else:
            self.fields['players'].queryset = User.objects.filter(role='player', player_teams__isnull=True)

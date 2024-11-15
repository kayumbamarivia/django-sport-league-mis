from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team1', 'team2', 'date', 'venue', 'league', 'score_team1', 'score_team2', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full py-2 px-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        team1 = cleaned_data.get('team1')
        team2 = cleaned_data.get('team2')
        
        if team1 == team2:
            raise forms.ValidationError("A team cannot play against itself.")
        return cleaned_data


from django import forms
from .models import League
from teams.models import Team 

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['name', 'start_date', 'end_date', 'teams']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'teams': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teams'].queryset = Team.objects.all()
        self.fields['teams'].help_text = "Hold down 'Control', or 'Command' on a Mac, to select multiple teams."

# forms.py
from django import forms
from .models import Team
from users.models import User

STYLES =  'form-input border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
class TeamForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(role='player'),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': STYLES,
            'id': 'id_players'  # Important for Select2 initialization
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

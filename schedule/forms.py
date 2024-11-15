from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['match', 'is_completed']
        widgets = {
            'match': forms.Select(attrs={
                'class': 'w-full py-2 px-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'w-6 h-6 text-blue-600 rounded focus:ring-2 focus:ring-blue-500'
            }),
        }

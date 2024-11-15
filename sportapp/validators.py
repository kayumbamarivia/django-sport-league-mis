# sportapp/validators.py
from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def validate(self, password, user=None):
        # Custom validation logic
        if not re.search(r'\d', password):  # password must contain at least one digit
            raise ValidationError("Password must contain at least one digit.")
    
    def get_help_text(self):
        return "Your password must contain at least one digit."

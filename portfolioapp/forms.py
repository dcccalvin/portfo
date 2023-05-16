from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_word_count(value):
    word_count = len(value.split())
    if word_count > 100:
        raise ValidationError(
            _('The text must be 100 words or fewer.'),
            params={'value': value},
        )
    
class project(forms.Form):
    name= forms.CharField(max_length=25)
    email=forms.EmailField(max_length=29)
    number=forms.IntegerField(max_length=12)
    description=forms.CharField(validate_word_count)
    
    def __str__(self):
        return self.name
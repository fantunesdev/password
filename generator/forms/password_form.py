from django import forms

from generator.models import Password


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['value', 'expiration_date', 'maximum_views']
        widgets = {
            'value': forms.HiddenInput(),
            'expiration_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'maximum_views': forms.NumberInput(attrs={'class': 'form-control'})
        }

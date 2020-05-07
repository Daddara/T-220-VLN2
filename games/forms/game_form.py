from django.forms import ModelForm, widgets
from games.models import Games


class GameUpdateForm(ModelForm):
    class Meta:
        model = Games
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'console': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'release_date': widgets.TextInput(attrs={'class': 'form-control'})
        }


class GameCreateForm(ModelForm):
    class Meta:
        model = Games
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'console': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'release_date': widgets.TextInput(attrs={'class': 'form-control'})
        }



from django import forms


class GameForm(forms.Form):
    GAME_CHOICES = (
        ('HeadsOrTails', 'Heads or Tails'),
        ('Cube', 'Cube'),
        ('RanNum', 'Random number'),
    )

    game = forms.ChoiceField(choices=GAME_CHOICES)
    count = forms.IntegerField(min_value=1, max_value=64)

from django.shortcuts import render
from . forms import GameForm
from . utils import HeadsOrTails, Cube, RanNum


def game_view(request):
    results = []
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game']
            game = globals()[game_type]()
            count = form.cleaned_data['count']
            for i in range(count):
                game.play()
                results.append(str(game))

    else:
        form = GameForm()

    return render(request, 'gameapp/games.html', {'form': form, 'results': results})

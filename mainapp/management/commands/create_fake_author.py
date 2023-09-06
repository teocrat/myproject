from django.core.management import BaseCommand
from mainapp.models import Author


class Command(BaseCommand):
    help = 'Create authors'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Author ID")

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            author = Author(name=f'Name{i}',
                            surname=f'Surname{i}',
                            email=f'Email{i}@example.com',
                            biography=f'{i} bla bla bla ',
                            bd='2003-07-12')
            author.save()

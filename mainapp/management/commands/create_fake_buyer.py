from django.core.management import BaseCommand
from mainapp.models import Buyer


class Command(BaseCommand):
    help = 'Create buyers'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Buyer ID")

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            buyer = Buyer(name=f'Buyer{i}',
                            email=f'Email{i}@example.com',
                            phone = f'+79863412{i}',
                            address=f'Address{i}',
                            )
            buyer.save()

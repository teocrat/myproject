from django.core.management import BaseCommand
from mainapp.models import Products


class Command(BaseCommand):
    help = 'Get all products'

    def handle(self, *args, **kwargs):
        products = Products.objects.all()

        self.stdout.write(f'{products}')
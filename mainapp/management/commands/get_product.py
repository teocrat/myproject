from django.core.management import BaseCommand
from mainapp.models import Products


class Command(BaseCommand):
    help = 'Get product'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Products.objects.get(pk=pk)

        self.stdout.write(f'{product}')
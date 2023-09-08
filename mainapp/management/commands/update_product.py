from django.core.management import BaseCommand
from mainapp.models import Products


class Command(BaseCommand):
    help = 'Update product`s price by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('price', type=str, help='Price')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')

        product = Products.objects.filter(pk=pk).first()
        product.price = price

        product.save()
        self.stdout.write('Done')
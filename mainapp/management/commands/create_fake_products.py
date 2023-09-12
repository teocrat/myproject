from django.core.management import BaseCommand
from mainapp.models import Products


class Command(BaseCommand):
    help = 'Create products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Product ID")

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            product = Products(product_name=f'Product{i}',
                               description=f'{i}.bla bla bla',
                               price=234.42 + i,
                               amount=20 + i,
                               )
            product.save()

from django.core.management import BaseCommand
from mainapp.models import Products


class Command(BaseCommand):
    help = "Delete product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Products.objects.filter(pk=pk).first()

        if product is not None:
            product.delete()
            self.stdout.write('Done')
        else:
            self.stdout.write('Product doesn`t exist')
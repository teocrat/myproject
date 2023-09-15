from django.core.management import BaseCommand
from mainapp.models import Orders, Buyer


class Command(BaseCommand):
    help = 'Create orders'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Order ID")

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for b in Buyer.objects.all()[:3]:
            for i in range(1, count + 1):
                order = Orders(
                    client=b,
                    sum_order=1000.54 + i,
                )
                order.save()

from django.core.management import BaseCommand
from mainapp.models import Post


class Command(BaseCommand):
    help = 'Get post'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Post ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.get(pk=pk)

        self.stdout.write(f'{post}')
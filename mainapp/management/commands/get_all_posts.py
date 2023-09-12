from django.core.management import BaseCommand
from mainapp.models import Post


class Command(BaseCommand):
    help = 'Get all posts'

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()

        self.stdout.write(f'{posts}')

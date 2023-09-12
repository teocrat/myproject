from django.core.management import BaseCommand
from mainapp.models import Post, Author


class Command(BaseCommand):
    help = 'Create post'

    def add_arguments(self, parser):
        parser.add_argument('author_pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        author_pk = kwargs.get('author_pk')
        a = Author.objects.all()[author_pk]

        post = Post(title='New post',
                    post='New bla bla bla',
                    date=f'2022-04-05',
                    author=a,
                    category=f'Category new', )
        post.save()

        self.stdout.write('Done')

       

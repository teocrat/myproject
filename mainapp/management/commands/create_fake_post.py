from django.core.management import BaseCommand
from mainapp.models import Author, Post


class Command(BaseCommand):
    help = 'Create posts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Author ID")

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for a in Author.objects.all():
            for i in range(1, count + 1):
                post = Post(title=f'Title{i}',
                            post=f'Post{i}',
                            date=f'2022-04-05',
                            author=a,
                            category=f'Category{i}',
                            published=True, )
                post.save()

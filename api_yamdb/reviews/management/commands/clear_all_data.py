from django.core.management import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if Title.objects.count() == 0:
            print('There are no rows in the table')
            return
        print("Delete all data...")
        Category.objects.all().delete()
        Comment.objects.all().delete()
        Genre.objects.all().delete()
        Title.objects.all().delete()
        Review.objects.all().delete()
        print('...done')

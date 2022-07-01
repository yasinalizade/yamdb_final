from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if Review.objects.count() > 1:
            print('all data already loaded...exiting.')
            return
        # Show this before loading the data into the database
        print('Loading all data...')
        # Code to load the data into database
        for row in DictReader(open(
                './static/data/category.csv', encoding='utf-8')):
            category = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug'],
            )
            category.save()

        for row in DictReader(open(
                './static/data/genre.csv', encoding='utf-8')):
            genre = Genre(
                id=row['id'],
                name=row['name'],
                slug=row['slug'],
            )
            genre.save()

        for row in DictReader(open(
                './static/data/titles.csv', encoding='utf-8')):
            title = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category'],
            )
            title.save()

        for row in DictReader(open(
                './static/data/genre_title.csv', encoding='utf-8')):
            title = Title.objects.get(id=row['title_id'])
            title.genre.add(row['genre_id'])
            title.save()

        for row in DictReader(open(
                './static/data/review.csv', encoding='utf-8')):
            review = Review(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author_id=row['author'],
                score=row['score'],
                pub_date=row['pub_date']
            )
            review.save()

        for row in DictReader(open(
                './static/data/comments.csv', encoding='utf-8')):
            comment = Comment(
                id=row['id'],
                review_id=row['review_id'],
                text=row['text'],
                author_id=row['author'],
                pub_date=row['pub_date']
            )
            comment.save()
        print('...done')

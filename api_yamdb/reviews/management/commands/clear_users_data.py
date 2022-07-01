from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if User.objects.count() == 0:
            print('There are no rows in the table')
            return
        print("Delete user data...")
        User.objects.exclude(id=1).delete()
        print('...done')

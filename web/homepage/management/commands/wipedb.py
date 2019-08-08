from django.core.management.base import BaseCommand, CommandError
from django.db import connection


class Command(BaseCommand):
    help = 'Wipes the database tables associated with Wagtail using a CASCADE to other tables'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute('''
              DELETE FROM wagtailcore_site CASCADE;
              DELETE FROM wagtailcore_grouppagepermission CASCADE;
              DELETE FROM wagtailcore_page CASCADE;
            ''')
            self.stdout.write(self.style.SUCCESS('Successfully wiped the tables'))

import os
import json
from django.core.management.base import BaseCommand
from library.models import Author  # Adjust the import based on your actual model location

class Command(BaseCommand):
    help = 'Populate authors for testing'

    def handle(self, *args, **options):
        file_path = os.path.join(os.getcwd(), 'authors.json')

        with open(file_path) as f:
            authors_data = json.load(f)

        for author_data in authors_data:
            Author.objects.create(
                name=author_data['name'],
                bio=author_data['bio']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated authors'))

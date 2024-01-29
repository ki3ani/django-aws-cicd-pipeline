import os
import json
from django.core.management.base import BaseCommand
from library.models import Book, Author  # Adjust the imports based on your actual model locations

class Command(BaseCommand):
    help = 'Populate books for testing'

    def handle(self, *args, **options):
        file_path = os.path.join(os.getcwd(), 'books.json')

        with open(file_path) as f:
            books_data = json.load(f)

        for book_data in books_data:
            author_id = book_data['author']
            author = Author.objects.get(pk=author_id)

            Book.objects.create(
                title=book_data['title'],
                author=author,
                description=book_data['description'],
                is_favorite=book_data['is_favorite']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated books'))

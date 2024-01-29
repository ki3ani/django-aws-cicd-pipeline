import os
import json
from django.core.management.base import BaseCommand
from library.models import Review, Book  # Adjust the imports based on your actual model locations

class Command(BaseCommand):
    help = 'Populate reviews for testing'

    def handle(self, *args, **options):
        file_path = os.path.join(os.getcwd(), 'reviews.json')

        with open(file_path) as f:
            reviews_data = json.load(f)

        for review_data in reviews_data:
            book_id = review_data['book']
            book = Book.objects.get(pk=book_id)

            Review.objects.create(
                book=book,
                review_text=review_data['review_text']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated reviews'))

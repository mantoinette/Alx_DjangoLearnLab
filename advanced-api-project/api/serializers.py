from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer serializes all fields of the Book model
# It includes validation to ensure the publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    # Custom validation for publication_year field
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(f"The publication year cannot be in the future. Current year is {current_year}.")
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']  # Include necessary fields here


# AuthorSerializer includes the author's name and a nested BookSerializer
# to dynamically serialize related books, along with book count
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    book_count = serializers.SerializerMethodField()

    # SerializerMethodField to dynamically calculate the number of books for an author
    def get_book_count(self, obj):
        return obj.books.count()

    class Meta:
        model = Author
        fields = ['id', 'name', 'books', 'book_count']  # Include necessary fields here

from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer serializes all fields of the Book model.
# It includes validation to ensure the publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):

    # Custom validation for publication_year field.
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

# AuthorSerializer includes the author's name and a nested BookSerializer
# to dynamically serialize related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

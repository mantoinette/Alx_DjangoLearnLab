from rest_framework import serializers
from bookshelf.models import Book  # Assuming your Book model is in the 'bookshelf' app

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

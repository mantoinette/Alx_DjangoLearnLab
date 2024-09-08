# api/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication (if using authentication)
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create some book objects for testing
        self.book1 = Book.objects.create(title="Django for Beginners", author="William S. Vincent", publication_year=2020)
        self.book2 = Book.objects.create(title="Two Scoops of Django", author="Daniel Roy Greenfeld", publication_year=2019)

        # Login the user (if using authentication)
        self.client.login(username='testuser', password='password123')

    def test_create_book(self):
        # Test creating a new book
        url = reverse('book-list')  # Assuming the list view name is 'book-list'
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2021}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_get_books(self):
        # Test retrieving the book list
        url = reverse('book-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        # Test updating a book
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'Django Mastery', 'author': 'William S. Vincent', 'publication_year': 2020}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Django Mastery')

    def test_delete_book(self):
        # Test deleting a book
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_search_books(self):
        # Test search functionality
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Django'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Django for Beginners')

    def test_filter_books(self):
        # Test filtering functionality
        url = reverse('book-list')
        response = self.client.get(url, {'author': 'Daniel Roy Greenfeld'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Daniel Roy Greenfeld')

    def test_order_books(self):
        # Test ordering functionality
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2019)  # Oldest book should come first

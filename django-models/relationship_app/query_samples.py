from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    # Get the author object by name
    author = Author.objects.get(name=author_name)
    
    # Retrieve all books associated with this author
    books = Book.objects.filter(author=author)
    return books


# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    # Get the library object based on its name
    library = Library.objects.get(name=library_name)
    
    # Explicitly get the librarian associated with this library
    librarian = Librarian.objects.get(library=library)
    
    return librarian




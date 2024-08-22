# Retrieve Operation

**Command:**
```python
# Retrieve the Book instance
book = Book.objects.get(id=book.id)
print("Retrieved book:", book.title, book.author, book.publication_year)

Expected Output:

Retrieved book: 1984 George Orwell 1949

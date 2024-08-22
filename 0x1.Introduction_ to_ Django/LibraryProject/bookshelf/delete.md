# Delete Operation

**Command:**
```python
from bookshelf.models import Book
# Delete the Book instance
book.delete()
print("Remaining books:", Book.objects.all())

Expected Output:
Remaining books: <QuerySet []>


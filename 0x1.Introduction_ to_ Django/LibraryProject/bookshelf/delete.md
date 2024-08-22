# Delete Operation

**Command:**
```python
# Delete the Book instance
book.delete()
print("Remaining books:", Book.objects.all())

Expected Output:
Remaining books: <QuerySet []>


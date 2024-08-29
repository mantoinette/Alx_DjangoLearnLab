<!-- list_books.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>List of Books</title>
</head>
<body>
    <h1>Books Available:</h1>
    <ul>
        {% for book in books %}
        <li>{{ book.title }} by {{ book.author.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>
<!-- library_detail.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Library Detail</title>
</head>
<body>
    <h1>Library: {{ library.name }}</h1>
    <h2>Books in Library:</h2>
    <ul>
        {% for book in library.books.all %}
        <li>{{ book.title }} by {{ book.author.name }} (Published {{ book.publication_year }})</li>
        {% endfor %}
    </ul>
</body>
</html>

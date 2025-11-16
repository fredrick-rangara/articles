# lib/article.py
from .author import Author
from .magazine import Magazine

class Article:
    all = []  # <-- CHANGED from _all_articles

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)  # <-- CHANGED from _all_articles

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError("Article title cannot be changed")
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = value

    def __repr__(self):
        return f"<Article '{self.title}' by {self.author.name}>"
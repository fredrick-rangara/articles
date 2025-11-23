from lib.author import Author
from lib.magazine import Magazine

class Article:
    # RENAMED to 'all' (lowercase) to match test file
    all = []

    def __init__(self, author, magazine, title):
        # Validation for initial values
        # Changed generic Exception to TypeError
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
            
        # Changed generic Exception to ValueError
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self) # Renamed

    # --- Properties ---

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        # Changed generic Exception to TypeError
        if not isinstance(new_author, Author):
            raise TypeError("Author must be an instance of Author")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        # Changed generic Exception to TypeError
        if not isinstance(new_magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        self._magazine = new_magazine
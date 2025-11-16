# lib/magazine.py

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        from .article import Article  # <-- Local import
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # This method uses .articles(), which handles its own import
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        mag_articles = self.articles()
        if not mag_articles:
            return None
        return [article.title for article in mag_articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        prolific_authors = [author for author, count in author_counts.items() if count > 2]
        
        return prolific_authors if prolific_authors else None

    @classmethod
    def top_publisher(cls):
        from .article import Article  # <-- Local import
        if not Article.all:
            return None
        
        top_mag = max(cls._all_magazines, key=lambda mag: len(mag.articles()))
        
        if len(top_mag.articles()) == 0:
            return None
            
        return top_mag

    def __repr__(self):
        return f'<Magazine {self.name} ({self.category})>'
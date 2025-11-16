# lib/author.py

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        from .article import Article  # <-- Local import
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # This method uses .articles(), which now handles its own import
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        from .article import Article  # <-- Local import
        return Article(self, magazine, title)

    def topic_areas(self):
        # This method uses .articles(), which handles its own import
        if not self.articles():
            return None
        return list(set(mag.category for mag in self.magazines()))

    def __repr__(self):
        return f'<Author {self.name}>'
# lib/magazine.py
# Removed module-level import for Article.
from collections import Counter 

class Magazine:
    ALL = []

    def __init__(self, name, category):
        # Initial validation
        # Changed generic Exception to ValueError
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
            
        # Changed generic Exception to ValueError
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        
        self._name = name
        self._category = category
        Magazine.ALL.append(self)

    # --- Properties ---

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # Changed generic Exception to ValueError
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        # Changed generic Exception to ValueError
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = new_category

    # --- Object Relationship Methods ---

    def articles(self):
        # Import Article only when the method is called
        from lib.article import Article
        # Using the corrected list name 'all'
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        # Import Article only when the method is called
        from lib.article import Article
        return list({article.author for article in self.articles()})

    # --- Aggregate and Association Methods ---

    def article_titles(self):
        if not self.articles():
            return None
            
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        # Uses self.articles(), which imports Article
        author_counts = Counter(article.author for article in self.articles())
        contributing = [author for author, count in author_counts.items() if count > 2]

        return contributing if contributing else None

    @classmethod
    def top_publisher(cls):
        # Import Article only when the method is called
        from lib.article import Article
        
        # Explicitly check for articles (using the corrected 'all' list)
        if not Article.all:
            return None

        # Logic only runs if articles exist
        magazine_counts = Counter(article.magazine for article in Article.all)
        top_magazine, _ = magazine_counts.most_common(1)[0]
        
        return top_magazine
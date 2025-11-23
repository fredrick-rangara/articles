# lib/author.py
# Removed module-level import for Article to break the circular dependency.

class Author:
    def __init__(self, name):
        # Initial validation
        # Changed generic Exception to ValueError
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")

        self._name = name

    # --- Properties ---

    @property
    def name(self):
        return self._name

    # --- Object Relationship Methods ---

    def articles(self):
        # Import Article only when the method is called
        from lib.article import Article 
        # Using the corrected list name 'all'
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        # Import Article only when the method is called
        from lib.article import Article 
        return list({article.magazine for article in self.articles()})

    # --- Aggregate and Association Methods ---

    def add_article(self, magazine, title):
        # Import necessary classes
        from lib.article import Article
        from lib.magazine import Magazine
        
        # Changed generic Exception to TypeError
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        
        # Article constructor handles title validation internally
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        
        return list({magazine.category for magazine in self.magazines()})
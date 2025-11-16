# tests/article_test.py
import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

class TestArticle:
    """Example tests for Article class"""

    def test_article_initialization(self):
        author = Author("George Orwell")
        mag = Magazine("Political Weekly", "Politics")
        article = Article(author, mag, "Animal Farm")
        
        assert article.author == author
        assert article.magazine == mag
        assert article.title == "Animal Farm"
        assert article in Article.all

    def test_title_is_immutable(self):
        author = Author("George Orwell")
        mag = Magazine("Political Weekly", "Politics")
        article = Article(author, mag, "Animal Farm")
        
        with pytest.raises(AttributeError):
            article.title = "1984"

    def test_title_validation(self):
        author = Author("Test Author")
        mag = Magazine("Test Mag", "Test")
        
        with pytest.raises(ValueError):
            Article(author, mag, "Too") # Too short
        with pytest.raises(ValueError):
            Article(author, mag, "This Title is Far Too Long for This Particular Requirement") # Too long
        with pytest.raises(ValueError):
            Article(author, mag, 123456) # Wrong type
            
    def test_author_can_be_changed(self):
        author_1 = Author("Author One")
        author_2 = Author("Author Two")
        mag = Magazine("Test Mag", "Test")
        article = Article(author_1, mag, "An Article")
        
        article.author = author_2
        assert article.author == author_2

    def test_author_type_validation(self):
        author = Author("Author One")
        mag = Magazine("Test Mag", "Test")
        article = Article(author, mag, "An Article")
        
        with pytest.raises(TypeError):
            article.author = "A string, not an author"

    def test_magazine_can_be_changed(self):
        author = Author("Test Author")
        mag_1 = Magazine("Mag One", "Test")
        mag_2 = Magazine("Mag Two", "Test")
        article = Article(author, mag_1, "An Article")
        
        article.magazine = mag_2
        assert article.magazine == mag_2

    def test_magazine_type_validation(self):
        author = Author("Test Author")
        mag = Magazine("Mag One", "Test")
        article = Article(author, mag, "An Article")
        
        with pytest.raises(TypeError):
            article.magazine = "A string, not a magazine"
# tests/magazine_test.py
import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

class TestMagazine:
    """Example tests for Magazine class"""
    
    def setup_method(self):
        """Clear data before each test method"""
        Article.all = []
        Magazine._all_magazines = []

    def test_magazine_initialization(self):
        mag = Magazine("Time", "News")
        assert mag.name == "Time"
        assert mag.category == "News"

    def test_name_is_mutable(self):
        mag = Magazine("Wired", "Tech")
        mag.name = "Wired Magazine"
        assert mag.name == "Wired Magazine"

    def test_name_validation(self):
        with pytest.raises(ValueError):
            Magazine("A", "Short") # Too short
        with pytest.raises(ValueError):
            Magazine("ThisNameIsWayTooLong", "Long") # Too long
        with pytest.raises(ValueError):
            Magazine(123, "Invalid") # Wrong type

    def test_category_is_mutable(self):
        mag = Magazine("GQ", "Style")
        mag.category = "Fashion"
        assert mag.category == "Fashion"

    def test_category_validation(self):
        with pytest.raises(ValueError):
            Magazine("Good Mag", "") # Empty
        with pytest.raises(ValueError):
            Magazine("Good Mag", 456) # Wrong type

    def test_contributors(self):
        author_1 = Author("Author 1")
        author_2 = Author("Author 2")
        mag = Magazine("Test Mag", "Testing")
        
        Article(author_1, mag, "Test Article 1")
        Article(author_2, mag, "Test Article 2")
        Article(author_1, mag, "Test Article 3") # Duplicate author
        
        assert len(mag.contributors()) == 2
        assert author_1 in mag.contributors()
        assert author_2 in mag.contributors()

    def test_article_titles(self):
        author = Author("Test Author")
        mag = Magazine("Test Mag", "Testing")
        
        assert mag.article_titles() is None # Test for no articles
        
        Article(author, mag, "Title One")
        Article(author, mag, "Title Two")
        
        titles = mag.article_titles()
        assert len(titles) == 2
        assert "Title One" in titles
        assert "Title Two" in titles

    def test_contributing_authors(self):
        author_1 = Author("Prolific Author")
        author_2 = Author("Occasional Author")
        author_3 = Author("Another Prolific")
        mag = Magazine("Test Mag", "Testing")

        assert mag.contributing_authors() is None # Test for no authors
        
        # Prolific Author 1: 3 articles
        Article(author_1, mag, "Title 1")
        Article(author_1, mag, "Title 2")
        Article(author_1, mag, "Title 3")
        
        # Occasional Author 2: 2 articles
        Article(author_2, mag, "Title 4")
        Article(author_2, mag, "Title 5")

        # Prolific Author 3: 4 articles
        Article(author_3, mag, "Title 6")
        Article(author_3, mag, "Title 7")
        Article(author_3, mag, "Title 8")
        Article(author_3, mag, "Title 9")

        prolific = mag.contributing_authors()
        assert len(prolific) == 2
        assert author_1 in prolific
        assert author_3 in prolific
        assert author_2 not in prolific
        
    def test_top_publisher(self):
        assert Magazine.top_publisher() is None # No articles at all
        
        author = Author("Test Author")
        mag_1 = Magazine("Mag 1", "Cat 1")
        mag_2 = Magazine("Mag 2", "Cat 2")
        mag_3 = Magazine("Mag 3", "Cat 3")
        
        assert Magazine.top_publisher() is None # Magazines exist, but no articles
        
        # Mag 1: 2 articles
        Article(author, mag_1, "Title 1")
        Article(author, mag_1, "Title 2")
        
        # Mag 2: 3 articles
        Article(author, mag_2, "Title 3")
        Article(author, mag_2, "Title 4")
        Article(author, mag_2, "Title 5")
        
        # Mag 3: 1 article
        Article(author, mag_3, "Title 6")
        
        assert Magazine.top_publisher() == mag_2
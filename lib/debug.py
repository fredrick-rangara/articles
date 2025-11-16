# lib/debug.py
import ipdb

# Import your classes
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

# Create some sample data
author_1 = Author("Carry Bradshaw")
author_2 = Author("Jack Kerouac")
mag_1 = Magazine("Vogue", "Fashion")
mag_2 = Magazine("Rolling Stone", "Music")

article_1 = Article(author_1, mag_1, "The New Look")
article_2 = Article(author_1, mag_1, "Men in Cities")
article_3 = Article(author_2, mag_2, "On the Road")

print("Starting debug session...")
print("Available variables:")
print("author_1, author_2")
print("mag_1, mag_2")
print("article_1, article_2, article_3")
print("Access classes: Author, Magazine, Article")

# This line starts the ipdb debugger
ipdb.set_trace()
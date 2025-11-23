# lib/debug.py

# Import necessary classes from your library files
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

# --- 1. Cleanup ---
# Optional: Clear any existing instances just in case the file is run multiple times
Article.ALL = []
Magazine.ALL = []

# --- 2. Create Sample Authors ---
print("Creating Authors...")
auth_jane = Author("Jane Smith")
auth_alex = Author("Alex Lee")
auth_chris = Author("Chris Doe")
print(f"Authors created: {auth_jane.name}, {auth_alex.name}, {auth_chris.name}")

# --- 3. Create Sample Magazines ---
print("Creating Magazines...")
mag_tech = Magazine("Tech Today", "Technology")
mag_food = Magazine("Gourmet Weekly", "Food & Drink")
mag_travel = Magazine("Wanderlust", "Travel")
print(f"Magazines created: {mag_tech.name}, {mag_food.name}, {mag_travel.name}")

# --- 4. Create Sample Articles (and establish relationships) ---
print("Creating Articles...")
# Jane (Contributes 3 to Tech, 1 to Food) -> Contributing Author Test
Article(auth_jane, mag_tech, "The Future of AI")
Article(auth_jane, mag_tech, "Python vs Javascript Speed")
Article(auth_jane, mag_tech, "Latest in Cloud Computing")
Article(auth_jane, mag_food, "Best Coffee Beans of 2025")

# Alex (Contributes 2 to Tech, 2 to Travel) -> Regular Contributor
Article(auth_alex, mag_tech, "5G Network Performance")
Article(auth_alex, mag_tech, "Quantum Hardware Explained")
Article(auth_alex, mag_travel, "A Week in Kyoto")
Article(auth_alex, mag_travel, "Hiking the Andes")

# Chris (Contributes 1 to Tech) -> Not a Contributing Author
Article(auth_chris, mag_tech, "Old School Programming")

print(f"Total articles created: {len(Article.ALL)}")

# --- 5. Test Aggregate Methods Manually ---
print("\n--- Testing Aggregate Methods ---")

# Author.topic_areas() test
print(f"{auth_jane.name}'s topics: {auth_jane.topic_areas()}") 
# Expected: ['Technology', 'Food & Drink']

# Magazine.contributing_authors() test
contributing = mag_tech.contributing_authors()
print(f"{mag_tech.name} contributing authors (>2 articles): {[a.name for a in contributing] if contributing else 'None'}") 
# Expected: ['Jane Smith']

# Magazine.top_publisher() test
top = Magazine.top_publisher()
print(f"Top Publisher: {top.name} with {len(top.articles())} articles")
# Expected: Tech Today (5 articles)

# --- 6. Drop into Debugger Session ---
# This is the line that starts the interactive session
import ipdb; ipdb.set_trace()
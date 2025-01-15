# Simple Fuzzy String Matching 

"""
One of the most popular packages for fuzzy string matching in Python is TheDuzz.
The Fuzz still holds as one of the most advance open-source libraries for fuzzy string
matching in Python.
It was first developed by SeatGeek for the purpose of distinguishing wheather two
ticket listings with similar names were forthe same event.

TheFuzz used the Levenshtein edit distance to calculate the degree of closeness between two strings.
It also provides features for determining string similarly in variaous 
situations.
"""
# First We must install thefuzz package. 

# pip install thefuzz 


# Simple ratio

"""We can determine the simple ratio between two strings using the ratio() method on the fuzz object.
This simply calculates the edit distance based on the ordering of both input strings
difflib.ratio()"""

# Check the similarity score 
import thefuzz 

from thefuzz import fuzz

name = "Kurtis Pykes"
full_name = "Kurtis K D Pykes"

print(f"Similarity score: {fuzz.ratio(name, full_name)}")



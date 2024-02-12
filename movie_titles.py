import re

# Test string
test_string = """Movie Titles:
Avengers (12)
The Shawshank Redemption (1994)
Casablanca (1942)
The Lord of the Rings: The Fellowship of the Ring (2001)
Spirited Away (2001)
Parasite (2019)"""

# Regex pattern to match Titles
titles_pattern = re.compile(r'.+ \(\d{4}\)')

# Test to see if pattern matches them correctly
if len(titles_pattern.findall(test_string)) != 0:
    print(f"Matches: {titles_pattern.findall(test_string)}")
else:
    print(f"{test_string} has no matches")
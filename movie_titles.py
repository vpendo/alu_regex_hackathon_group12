import re

# Test string
test_string = """Movie Titles:
Reacher (12)
Game of Thrones (1993)
Casablanca (1942)
The Lord of the Rings: The Fellowship of the Ring (2001)
The Orginals (2001)
legacies (2019)"""

# Regex pattern to match Titles
titles_pattern = re.compile(r'.+ \(\d{4}\)')

# Test to see if pattern matches them correctly
if len(titles_pattern.findall(test_string)) != 0:
    print(f"Matches: {titles_pattern.findall(test_string)}")
else:
    print(f"{test_string} has no matches")

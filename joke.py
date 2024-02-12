import re

# Test string
test_string = """Why did the scarecrow win an award? Because he was outstanding in his field!
How do you make a tissue dance? Put a little boogie in it!
What do you call a lazy kangaroo? Pouch potato!
What do you call a fish with no eyes? Fsh!
Why did the bicycle fall over? Because it was two tired!"""

# Regex pattern to match Joke patterns
Joke_pattern = re.compile(r'Why did the .* ? Because.*')

# Test to see if pattern matches them correctly
if len(Joke_pattern.findall(test_string)) != 0:
    print(f"Matches: {Joke_pattern.findall(test_string)}")
else:
    print(f"{test_string} has no matches")
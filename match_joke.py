import re

# Test string
test_string = """Why did the Dodge car bring a ladder to the race? To take the competition to a whole new level!
Because when life throws curves, dodge them with a wink and a rev! From the speed demon Challenger to the powerhouse Charger, find your thrill on every road twist."""

# Regex pattern to match Joke patterns
Joke_pattern = re.compile(r'Why did the .* ? Because.*')

# Test to see if pattern matches them correctly
if len(Joke_pattern.findall(test_string)) != 0:
    print(f"Matches: {Joke_pattern.findall(test_string)}")
else:
    print(f"{test_string} has no matches")
import re

# Test string
test_string = """[Verse 1] The world is spinning 'round and 'round
[Verse 2] We're dancing on the edge of something new
[Verse 3] But don't you worry, we'll be alright
[Outro] So hold on tight, and let's fly
[Rap Verse 1] Yo, check it, the beat is bumpin'"""

# Regex pattern to match song lyrics
lyrics_pattern = re.compile(r'\[Verse \d+\].+')

# Test to see if pattern matches them correctly
if len(lyrics_pattern.findall(test_string)) != 0:
    print(f"Matches: {lyrics_pattern.findall(test_string)}")
else:
    print(f"{test_string} has no matches")
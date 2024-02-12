import re

# Define the test string
test_string = """[1st verse] i'm the door open i'm leave the door open girl
[2nd verse] open can't you see that i am coming through
[3nd verse] yeah i love it when you say 
[Outro] come closer
[Rnb 1st verse] you better not change'"""

# Define the regular expression pattern to match song lyrics
lyrics_pattern = re.compile(r'\[(\d+)(?:st|nd|rd|th) verse\].+')

# Find all matches of the pattern in the test string
matches = lyrics_pattern.findall(test_string)

# Check if there are any matches and print them
if matches:
    print(f"Matches: {matches}")
else:
    print(f"No matches found in the test string.")
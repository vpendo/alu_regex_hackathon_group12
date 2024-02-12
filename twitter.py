import re

# Define the test string
test_string = """Twitter Handles:
#soccer
@michaeljrd
@FBI
@TF1
@migos
@GretaThunberg"""

# Define the regular expression pattern to match Twitter usernames
twitter_pattern = re.compile(r'@\w+')

# Find all matches of the pattern in the test string
matches = twitter_pattern.findall(test_string)

# Check if there are any matches and print them
if matches:
    print(f"Matches: {matches}")
else:
    print(f"No matches found in the test string.")

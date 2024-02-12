import re

# Regex pattern to match joke patterns
joke_pattern = re.compile(r'Why did the .*? Because .*?')

# Prompt the user to enter their joke
user_joke = input("Enter your joke: ")

# Test to see if pattern matches the user-provided joke
if len(joke_pattern.findall(user_joke)) != 0:
    print("Match found!")
else:
    print("No match found.")



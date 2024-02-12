import re

# Regex pattern to match hex color codes
color_pattern = re.compile(r'#[A-Fa-f0-9]{6}')

# Prompt the user to enter the color codes
user_input = input("Enter the color codes: ")

# Test to see if pattern matches the user-provided color codes
matches = color_pattern.findall(user_input)
if len(matches) != 0:
    print(f"Matches: {matches}")
else:
    print("No matches found.")

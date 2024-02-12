import re

# Test string
test_string = """Hex Color Codes:
#FF001
#FF0000
#FFFFFF
#333333
#C0C0C0
#808080"""

# Regex pattern to match hex color codes
color_pattern = re.compile(r'#[A-Fa-f0-9]{6}')

# Test to see if pattern matches them correctly
if len(color_pattern.findall(test_string)) != 0:
    print(f"Matches: {color_pattern.findall(test_string)}")
else:
    print(f"{test_string} has no matches")
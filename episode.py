import re

# The pattern
episode_title_pattern = r".+ S\d{2}E\d{2}:.+"

# Test strings
test_strings = [
    "Indeed S03E04: Inside the room",
    "Game of Thrones S012E04: The Knight of the night",
    "Come on  S05E02: Infusion",
    "Breaking Bad S05E14: Irrelevant",
    "Tree: Inside"
]

# Test the pattern
for test_string in test_strings:
    if re.match(episode_title_pattern, test_string):
        print(f"{test_string}: matches the pattern")
    else:
        print(f"{test_string}: does not match the pattern")

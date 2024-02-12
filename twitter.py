import re

# Test string
test_string = """Twitter Handles:
#NBA
@elonmusk
@NASA
@NatGeo
@BTS_twt
@GretaThunberg"""

# Regex pattern to match twitter usernames
usernames_pattern = re.compile(r'@\w+')

# Test to see if pattern matches them correctly
if len(usernames_pattern.findall(test_string)) != 0:
    print(f"Matches: {usernames_pattern.findall(test_string)}")
else:
    print(f"{test_string} has no matches")
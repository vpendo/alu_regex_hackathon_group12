import re

# Regex to find dates
date = re.compile(r'\d{2}-[a-zA-z]{3}-\d{4}')

# Prompt the user to enter the text
user_text = input("Enter the date, for example [02-feb-2002]: ")

# Test to see if pattern matches dates in the user-provided text
results = date.findall(user_text)
if len(results) != 0:
    print(f"Matches: {results}")
else:
    print("No matches found.")


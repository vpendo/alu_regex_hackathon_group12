import re

# Regex pattern to match IP addresses
ip_pattern = re.compile(r'((?:(?:[01]?\d{1,2}|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d{1,2}|2[0-4]\d|25[0-5])(?=\D|$))')

# Prompt the user to enter the text containing IP addresses
user_input = input("Enter the text containing IP addresses, for example [192.168.1.1]: ")

# Test to see if pattern matches the user-provided text
matches = ip_pattern.findall(user_input)
if len(matches) != 0:
    print(f"Matches: {matches}")
else:
    print("No matches found.")
